#!/usr/bin/env python3
"""Local-first AI Video Ad Lab CLI; standard library only."""
from __future__ import annotations
import argparse, csv, hashlib, json, re, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "06_PROJECTS"
REGISTRY = ROOT / "10_REGISTRY"
TEMPLATE = ROOT / "05_TEMPLATES"

def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def load(path, errors):
    try:
        return json.loads(path.read_text(encoding="utf8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")
        return None

def ids(pattern, paths):
    found=[]
    for p in paths:
        m=re.fullmatch(pattern, p.name)
        if m: found.append(int(m.group(1)))
    return found

def next_id(prefix, paths):
    pattern=re.escape(prefix)+r"(\d{4})(?:_|$)"
    nums=[]
    for path in paths:
        match=re.match(pattern, path.name)
        if match:
            nums.append(int(match.group(1)))
    return f"{prefix}{max(nums,default=0)+1:04d}"

def slugify(value):
    s=re.sub(r"[^a-z0-9]+","_",value.lower()).strip("_")
    return s or "untitled"

def project_dirs():
    return sorted(p for p in PROJECTS.iterdir() if p.is_dir() and re.fullmatch(r"P\d{4}_.+",p.name))

def copy_template(dst):
    shutil.copytree(TEMPLATE/"PROJECT_TEMPLATE",dst,ignore=shutil.ignore_patterns("__pycache__"))

def write_status(project, stage="STAGE_00", approved="none", blocked="none", next_action="register inputs and execute Intake", package="none"):
    text=f"# Project status\n\n- Current stage: {stage}\n- Approved: {approved}\n- Blocked: {blocked}\n- Next action: {next_action}\n- Next prompt package: {package}\n- Files that matter now: project.json, 00_BRIEF/brief.md, 01_INPUTS/README.md\n"
    (project/"STATUS.md").write_text(text,encoding="utf8")

def rebuild_registry():
    errors=[]; projects=[]; runs=[]; experiments=[]; learnings=[]; changes=[]
    for p in project_dirs():
        meta=load(p/"project.json",errors)
        if meta:
            projects.append({k:meta.get(k,"") for k in ["project_id","slug","title","status","current_stage","updated_at"]})
        for r in sorted((p/"12_RUNS").glob("*/run.json")):
            m=load(r,errors)
            if m:
                ev=m.get("evaluation",{})
                runs.append({"run_id":m.get("run_id",""),"project_id":m.get("project_id",""),"stage":m.get("stage",""),"task":m.get("task",""),"tool":m.get("tool",""),"model":m.get("model",""),"evaluation_status":ev.get("status",""),"overall_score":ev.get("overall_score",""),"selected":m.get("selected",False)})
    for p in sorted((ROOT/"07_EXPERIMENTS").glob("EXP-*/experiment.json")):
        m=load(p,errors)
        if m: experiments.append({k:m.get(k,"") for k in ["experiment_id","status","task","confidence"]})
    for kind, key, target in [("validated_learnings","learning_id",learnings),("change_proposals","change_id",changes)]:
        for p in sorted((ROOT/"09_LEARNING"/kind).glob("*.md")):
            m=re.match(r"(LRN|CHG)-\d{4}",p.stem)
            if m: target.append({key:m.group(0),"confidence":"","title":p.stem,"path":str(p.relative_to(ROOT))} if key=="learning_id" else {key:m.group(0),"status":"","title":p.stem,"path":str(p.relative_to(ROOT))})
    prompts=[]
    for p in sorted((ROOT/"02_PROMPT_SYSTEM/library").glob("*.md")):
        raw=p.read_text(encoding="utf8")
        pid=re.search(r"prompt_id:\s*(\S+)",raw); ver=re.search(r"version:\s*(\S+)",raw); status=re.search(r"status:\s*(\S+)",raw); task=re.search(r"task:\s*(\S+)",raw)
        if pid: prompts.append({"prompt_id":pid.group(1),"version":ver.group(1) if ver else "","status":status.group(1) if status else "","task":task.group(1) if task else "","path":str(p.relative_to(ROOT))})
    tools=[]
    for p in sorted((ROOT/"03_TOOL_KNOWLEDGE").glob("*/*.md")):
        raw=p.read_text(encoding="utf8")
        tid=re.search(r"tool_id:\s*(\S+)",raw)
        if tid:
            get=lambda k: (re.search(k+r":\s*(\S+)",raw).group(1) if re.search(k+r":\s*(\S+)",raw) else "")
            tools.append({"tool_id":tid.group(1),"tool_name":get("tool_name"),"category":get("category"),"verification_status":get("verification_status"),"last_verified":get("last_verified")})
    specs={"projects":projects,"runs":runs,"prompts":prompts,"tools":tools,"experiments":experiments,"learnings":learnings,"changes":changes}
    headers={"projects":["project_id","slug","title","status","current_stage","updated_at"],"runs":["run_id","project_id","stage","task","tool","model","evaluation_status","overall_score","selected"],"prompts":["prompt_id","version","status","task","path"],"tools":["tool_id","tool_name","category","verification_status","last_verified"],"experiments":["experiment_id","status","task","confidence"],"learnings":["learning_id","confidence","title","path"],"changes":["change_id","status","title","path"]}
    for n,rows in specs.items():
        with (REGISTRY/(n+".csv")).open("w",newline="",encoding="utf8") as f:
            w=csv.DictWriter(f,fieldnames=headers[n]);w.writeheader();w.writerows(rows)
    return errors, specs

def dashboard(specs=None):
    if specs is None: _,specs=rebuild_registry()
    active=[p for p in specs["projects"] if p.get("status")=="active"]
    candidates=[p for p in specs["prompts"] if p.get("status")=="candidate"]
    openexp=[e for e in specs["experiments"] if e.get("status") not in ("complete","cancelled")]
    text="# AI Video Ad Lab dashboard\n\n"
    text+=f"- System version: {(ROOT/'VERSION').read_text().strip()}\n- Active projects: {len(active)}\n- Project current stages: "+(", ".join(f"{x['project_id']} {x['current_stage']}" for x in active) or "none")+"\n"
    text+=f"- Pending approvals: inspect active STATUS files\n- Open experiments: {len(openexp)}\n- Prompt candidates awaiting validation: {len(candidates)}\n- Recent validated learnings: {len(specs['learnings'])}\n- Pending system change proposals: {len(specs['changes'])}\n- Recent failures by category: recorded in Run reviews; aggregate not yet implemented\n- Next recommended action: "+("advance active project gate" if active else "create first real project and register inputs")+"\n\nGenerated by lab.py dashboard; not source of truth.\n"
    (ROOT/"DASHBOARD.md").write_text(text,encoding="utf8")

def validate():
    errors=[]
    for n in ["AGENTS.md","README.md","START_HERE.md","DASHBOARD.md","CHANGELOG.md","VERSION"]:
        if not (ROOT/n).is_file(): errors.append("Missing root file "+n)
    seen=set()
    for p in project_dirs():
        m=load(p/"project.json",errors)
        if not m: continue
        pid=m.get("project_id")
        if not re.fullmatch(r"P\d{4}",str(pid)): errors.append(f"Bad project_id {p}")
        if pid in seen: errors.append("Duplicate project ID "+str(pid))
        seen.add(pid)
        sel=m.get("selected_final_run")
        runids=set()
        for r in (p/"12_RUNS").glob("*/run.json"):
            x=load(r,errors)
            if not x: continue
            rid=x.get("run_id");runids.add(rid)
            if not re.fullmatch(re.escape(str(pid))+r"-R\d{4}",str(rid)): errors.append(f"Bad run ID {r}")
            if x.get("selected") and x.get("evaluation",{}).get("overall_score") is None: errors.append(f"Selected Run missing evaluation {rid}")
        if sel and sel not in runids: errors.append(f"Missing selected run {sel} in {pid}")
    preg=ROOT/"02_PROMPT_SYSTEM/registry/prompt_registry.json"
    pm=load(preg,errors)
    if pm:
        for x in pm.get("prompts",[]):
            if not x.get("prompt_id") or not x.get("version"): errors.append("Canonical prompt missing ID/version")
            if not (ROOT/x.get("path","")).is_file(): errors.append("Missing prompt path "+str(x.get("path")))
    drift,_=rebuild_registry()
    errors.extend(drift)
    if errors:
        print("VALIDATION FAILED")
        print("\n".join("- "+e for e in errors));return 1
    print("Validation passed.");return 0

def hash_assets(project=None):
    roots=[PROJECTS/project] if project else project_dirs()
    count=0
    for root in roots:
        if not root.exists(): raise SystemExit("Unknown project "+str(root))
        assets=[]
        for p in root.rglob("*"):
            if p.is_file() and p.suffix.lower() in {".jpg",".jpeg",".png",".webp",".mp4",".mov",".wav"}:
                h=hashlib.sha256(p.read_bytes()).hexdigest()
                assets.append({"path":str(p.relative_to(root)),"sha256":h,"bytes":p.stat().st_size});count+=1
        (root/"asset_manifest.json").write_text(json.dumps({"generated_at":now(),"assets":assets},indent=2)+"\n",encoding="utf8")
    print(f"Hashed {count} assets.")

def new_project(args):
    pid=next_id("P",[p for p in PROJECTS.iterdir() if p.is_dir()])
    slug=slugify(args.slug or args.title); dst=PROJECTS/(pid+"_"+slug)
    copy_template(dst)
    m=load(dst/"project.json",[]) or {}
    m.update({"project_id":pid,"slug":slug,"title":args.title,"status":"active","created_at":now(),"updated_at":now(),"current_stage":"STAGE_00"})
    if args.duration: m["deliverable"]["duration_seconds"]=args.duration
    if args.aspect: m["deliverable"]["aspect_ratio"]=args.aspect
    (dst/"project.json").write_text(json.dumps(m,indent=2)+"\n",encoding="utf8")
    write_status(dst); rebuild_registry(); dashboard()
    print(f"Created {dst.relative_to(ROOT)}")

def new_experiment(args):
    eid=next_id("EXP-",[p for p in (ROOT/"07_EXPERIMENTS").iterdir() if p.is_dir()]);dst=ROOT/"07_EXPERIMENTS"/eid
    shutil.copytree(TEMPLATE/"EXPERIMENT_TEMPLATE",dst)
    p=dst/"experiment.json";m=load(p,[]) or {};m.update({"experiment_id":eid,"status":"planned","task":args.task or "unknown"});p.write_text(json.dumps(m,indent=2)+"\n",encoding="utf8")
    rebuild_registry();dashboard();print(f"Created {dst.relative_to(ROOT)}")

def status(pid):
    p=next((x for x in project_dirs() if x.name.startswith(pid+"_")),None)
    if not p: raise SystemExit("Unknown project "+pid)
    print((p/"STATUS.md").read_text(encoding="utf8"))

def main():
    ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest="cmd",required=True)
    q=sub.add_parser("new-project");q.add_argument("title");q.add_argument("--slug");q.add_argument("--duration",type=int);q.add_argument("--aspect");q.set_defaults(fn=new_project)
    q=sub.add_parser("new-experiment");q.add_argument("--task");q.set_defaults(fn=new_experiment)
    q=sub.add_parser("validate");q.set_defaults(fn=lambda a: sys.exit(validate()))
    q=sub.add_parser("rebuild-registry");q.set_defaults(fn=lambda a: (rebuild_registry(),print("Registries rebuilt.")))
    q=sub.add_parser("dashboard");q.set_defaults(fn=lambda a: (dashboard(),print("Dashboard updated.")))
    q=sub.add_parser("hash-assets");q.add_argument("project",nargs="?");q.set_defaults(fn=lambda a: hash_assets(a.project))
    q=sub.add_parser("project-status");q.add_argument("project");q.set_defaults(fn=lambda a: status(a.project))
    a=ap.parse_args();a.fn(a)
if __name__=="__main__":main()

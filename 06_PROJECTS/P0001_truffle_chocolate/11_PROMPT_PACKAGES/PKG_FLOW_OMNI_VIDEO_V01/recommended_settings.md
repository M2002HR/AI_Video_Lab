# Recommended run setup — P0001 Flow Omni video v01

## Target
- Tool: Google Flow
- Model: Gemini Omni Flash
- Mode: Ingredients / references to video
- Duration: 10 seconds
- Aspect ratio: 16:9

## Ingredients
Upload exactly the five images listed in `references.md`, in that order.
Do not fill slots 6–7 in the first controlled run.

## Controlled-run rule
Generate **two initial video candidates with identical inputs**:
- same five ingredient images;
- same upload order;
- same prompt;
- same exposed settings/defaults.

Do not change prompt or ingredient stack between the first two runs.
The purpose is to measure baseline stability before optimization.

## UI/settings discipline
Record every setting actually exposed in the Flow UI.
Do not assume a textual prompt statement changes technical file properties unless Flow exposes the control.
Do not invent or change unrelated settings between the two baseline runs.

## Audio
The prompt requests no dialogue/voiceover and only unobtrusive ambience if native audio is generated.
If Flow exposes an audio control, record its state in the Run metadata; otherwise leave the tool default unchanged for the first controlled pair.

## Expected run IDs
- `P0001-R0022`
- `P0001-R0023`

After generation, export/download both videos and provide them for frame-by-frame QA before any prompt revision.

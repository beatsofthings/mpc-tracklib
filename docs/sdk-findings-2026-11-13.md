# Official Akai SDK review — 2026-11-13

Source: https://github.com/inmusic-software/mpc-plugin-builder-sdk

Reviewed upstream `README.md`, `docs/overview.md` and `docs/ui-reference.md`.

## Confirmed

- MPC Live III is an ARM64 target and requires MPC OS 3.10.1+ with External Plugin Support enabled.
- Plugins are VST2 `.so` libraries loaded inside the MPC application, without isolated crash protection.
- The MPC hardware has **no plugin windows**. Its UI is a JSON-described scripted skin (`TUI.json`) of widgets, images, controls, tabs and parameter bindings.
- The SDK's generated UI consists of parameter controls; custom skins may place images and supported widgets but are not HTML/JavaScript browser windows.
- The official docs do **not** document an embeddable WebKit/Chromium webview or arbitrary browser framebuffer integration.

## Consequence

A standard web browser cannot simply be wrapped as an official SDK plugin. No working webview is demonstrated. The unchanged Tracklib website requirement remains unmet with documented SDK features.

## Next investigation

Look for a separately supported MPC OS app/browser interface. If none exists, ask Akai whether browser UI surfaces are planned, and Tracklib whether embedded-browser access is permitted. Do not ship a mock interface or unsupported framebuffer hack as a working browser.

## Build status

No official SDK build or MPC hardware test has been executed. The SDK source was inspected through the connected GitHub integration; direct clone into the execution container was blocked by DNS resolution.

# MPC Live III — Browser investigation

## Evidence (2026-11-13)

- Official SDK: https://github.com/inmusic-software/mpc-plugin-builder-sdk — VST2 plugin loaded in MPC process, JSON-defined touch UI, no plugin windows.
- OpenMPC Plugin Manager: https://open-mpc.github.io/mpc-vst-plugins/install.html — plugin with a web UI accessed from phone/computer on local Wi-Fi; **not** proof of a webview on the MPC display.

## Candidate A: official SDK

Documented skin widgets do not include a general HTML/JS browser surface. This path cannot currently satisfy unchanged Tracklib website on the device. Do not claim a working browser.

## Candidate B: standalone Linux browser

Research only; no firmware modifications planned. Unknowns:

1. MPC Live III display server/compositor, framebuffer and touch input ownership.
2. Whether an ARM64 browser runtime with required libraries can run without destabilizing MPC OS.
3. Supported app launching and switching back to the MPC application.
4. TLS/certificates, cookies, persistent sessions, audio preview, memory/CPU budget.
5. Safe download destination on removable storage and import into MPC sample editor.
6. Tracklib policy on embedded-browser sign-in and purchasing.

## Go/no-go experiment

First obtain read-only system inventory from a test device or published official documentation; do not stop the MPC application or install system packages. If supported browser integration is unavailable, stop and consult Akai/Tracklib rather than bypassing OS protections.

## User-facing promise

The project must not replace Tracklib's purchase flow or store credentials. No automatic purchases. No claim that using the original website alone resolves licensing and platform terms.

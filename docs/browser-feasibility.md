# MPC Tracklib: native browser feasibility

Goal: display the unchanged https://www.tracklib.com website on Akai MPC Live III. Tracklib itself handles sign-in, credit confirmations and licensing. No scraping, reverse-engineered endpoints or credential capture.

**Status: feasibility investigation, not a working browser.**

## Test gates

- [ ] Review official Akai MPC 3.10.1 Plugin SDK and sample code.
- [ ] Check if a plugin can render a browser framebuffer and receive touchscreen input.
- [ ] Check network/TLS and availability of a supported WebKit/Chromium runtime on the MPC.
- [ ] Check persistent cookies and whether Tracklib permits embedded-browser sign-in.
- [ ] Check authorized download to user-selected SD/USB storage.
- [ ] Check opening a downloaded WAV in the MPC sample editor.

## First executable milestone

Build an SDK plugin that displays a locally generated test surface and handles a touch event. Only then consider browser integration.

## Boundaries

Do not assume a browser is legally unrestricted merely because it shows the original site. Respect Tracklib terms and Akai SDK restrictions. Do not modify firmware or bypass site restrictions without a separate explicit decision.

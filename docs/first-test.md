# Test 1 — Akai SDK browser capability

This repository intentionally does **not** claim that an embedded browser works on MPC Live III.

## Reproducible SDK inspection

When an official Akai SDK distribution is available in the development environment:

```sh
python tools/check_sdk_browser.py /path/to/extracted/akai-sdk
```

This is a read-only keyword inventory, **not** a compile or hardware test.

## Required evidence before implementation

1. Exact SDK version, license, supported plugin types and ARM target.
2. Public SDK API or documented mechanism for arbitrary web-content rendering.
3. Touch event dispatch and a supported browser runtime (not just DSP/UI parameters).
4. Network access, TLS trust store, cookies and persistent session behavior.
5. Approved file-writing paths and whether downloaded audio can be imported into MPC's sample browser.
6. Tracklib's permission for embedded webviews and login compatibility.

## Go/no-go

If a supported browser surface does not exist, do not represent a mock screen or external browser as an embedded MPC browser. Record the blocker and evaluate other supported approaches.

## User acceptance test (only after capability confirmed)

Open https://www.tracklib.com in the MPC UI, log in through Tracklib, preview a song, confirm an authorized purchase and download to user storage. Never collect credentials in plugin code or automate a purchase.

# Webview feasibility verdict — 2026-11-13

Official SDK: https://github.com/inmusic-software/mpc-plugin-builder-sdk

## Result

The SDK targets in-process VST2 instruments/effects, with scripted JSON UI skins. Its documented plugin UI is not a general windowing API and does not offer a documented HTML webview, Chromium/WebKit host, or browser surface. Therefore **the unchanged Tracklib website cannot currently be implemented through the documented official SDK alone**. This is a limitation of the available documented API, not proof that any possible unsupported system hack is impossible.

## Additional evidence

The OpenMPC Plugin Manager has a browser-based management UI that can be opened on a phone or computer; this does not demonstrate a full browser rendered on the MPC touchscreen. See https://github.com/open-mpc/mpc-vst-plugins and https://open-mpc.github.io/mpc-vst-plugins/faq.html .

## No-SSH plan

1. Avoid installing untested browser binaries or touching MPC OS internals.
2. Request from Akai a supported webview/custom rendering API or standalone app extension point.
3. Request from Tracklib permission for an embedded browser login and direct user-authorized downloads.
4. If Akai confirms a supported API, create a minimal hello-world rendering and touch test, then integrate the original Tracklib URL.
5. Otherwise, treat original-site-on-MPC as blocked; do not substitute a fake UI.

No compiled plugin or hardware browser test has been completed.

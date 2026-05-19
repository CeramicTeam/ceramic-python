# Changelog

## 2.3.1 (2026-05-13)

Full Changelog: [v2.3.0...v2.3.1](https://github.com/CeramicTeam/ceramic-python/compare/v2.3.0...v2.3.1)

## 2.3.0 (2026-05-12)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/CeramicTeam/ceramic-python/compare/v2.2.0...v2.3.0)

### Features

* add maxDescriptionLength parameter ([8ea839c](https://github.com/CeramicTeam/ceramic-python/commit/8ea839c96d46ac2c60ad25e2c6e1da75c9f34c46))

## 2.2.0 (2026-05-12)

Full Changelog: [v2.1.1...v2.2.0](https://github.com/CeramicTeam/ceramic-python/compare/v2.1.1...v2.2.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([9e2f194](https://github.com/CeramicTeam/ceramic-python/commit/9e2f1942eccd4f4e407ee4d16ab651665605625d))

## 2.1.1 (2026-05-09)

Full Changelog: [v2.1.0...v2.1.1](https://github.com/CeramicTeam/ceramic-python/compare/v2.1.0...v2.1.1)

### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([02a75c8](https://github.com/CeramicTeam/ceramic-python/commit/02a75c84ada66845d9d70f369abe11fe476b943e))

## 2.1.0 (2026-05-01)

Full Changelog: [v2.0.2...v2.1.0](https://github.com/CeramicTeam/ceramic-python/compare/v2.0.2...v2.1.0)

### Features

* support setting headers via env ([dff4dc8](https://github.com/CeramicTeam/ceramic-python/commit/dff4dc8446469b3b6dde7f6f2677a7bd3e3f6928))


### Bug Fixes

* use correct field name format for multipart file arrays ([101906b](https://github.com/CeramicTeam/ceramic-python/commit/101906b38d2aeffe5e6111a8f8778210db470f71))


### Chores

* **internal:** reformat pyproject.toml ([d4bd478](https://github.com/CeramicTeam/ceramic-python/commit/d4bd47804aaa4d05491a9a6defcf327ab298f408))

## 2.0.2 (2026-04-23)

Full Changelog: [v2.0.1...v2.0.2](https://github.com/CeramicTeam/ceramic-python/compare/v2.0.1...v2.0.2)

### Chores

* **internal:** more robust bootstrap script ([a01b77e](https://github.com/CeramicTeam/ceramic-python/commit/a01b77e005fdfc6d52da2f22436fa11bcd8535b6))

## 2.0.1 (2026-04-18)

Full Changelog: [v2.0.0...v2.0.1](https://github.com/CeramicTeam/ceramic-python/compare/v2.0.0...v2.0.1)

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([88d9f55](https://github.com/CeramicTeam/ceramic-python/commit/88d9f55663b288f9c85c65581a20d04183a527a3))

## 2.0.0 (2026-04-17)

Full Changelog: [v1.2.1...v2.0.0](https://github.com/CeramicTeam/ceramic-python/compare/v1.2.1...v2.0.0)

### Features

* Updating main with staging ([14788dd](https://github.com/CeramicTeam/ceramic-python/commit/14788dd44074e9a94986bacfd364ceb1d8227bf4))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([07e8d4b](https://github.com/CeramicTeam/ceramic-python/commit/07e8d4bf9f97ec8cf15641e4d9bbe94f5ad23580))
* ensure file data are only sent as 1 parameter ([6f87619](https://github.com/CeramicTeam/ceramic-python/commit/6f87619321106741c8437af3139a22a0b863dc77))


### Chores

* **ci:** remove release-doctor workflow ([a3eb54d](https://github.com/CeramicTeam/ceramic-python/commit/a3eb54d0b124d2187ad0451d1709e5b18610fa35))

## 1.2.1 (2026-04-07)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/CeramicTeam/ceramic-python/compare/v1.2.0...v1.2.1)

### Features

* Update main with staging ([9535c77](https://github.com/CeramicTeam/ceramic-python/commit/9535c77eaf07a0cf4c1747e70a5486c93309deac))

## 1.2.0 (2026-03-30)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/CeramicTeam/ceramic-python/compare/v1.1.0...v1.2.0)

### Features

* **internal:** implement indices array format for query and form serialization ([1a2e0b3](https://github.com/CeramicTeam/ceramic-python/commit/1a2e0b38698193088625bedec62a395a161641ad))
* **python-sdk:** add client-side validation for search query word count ([3c1d67c](https://github.com/CeramicTeam/ceramic-python/commit/3c1d67ce0167e6b3eb9513c42c0357e5f8fd90c0))
* Update main with staging ([2f0e5f9](https://github.com/CeramicTeam/ceramic-python/commit/2f0e5f9df377c9a79e9858c1fb190a255f5c045d))

## 1.1.0 (2026-03-27)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/CeramicTeam/ceramic-python/compare/v1.0.0...v1.1.0)

### Features

* Update main with staging ([7036740](https://github.com/CeramicTeam/ceramic-python/commit/703674073c7d43a12665247aa2a2f4741c5320e4))

## 1.0.0 (2026-03-26)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/CeramicTeam/ceramic-python/compare/v0.0.1...v1.0.0)

### ⚠ BREAKING CHANGES

* change API base path to /search

### Bug Fixes

* change API base path to /search ([aabc864](https://github.com/CeramicTeam/ceramic-python/commit/aabc8645cf73e645279bf2c3b9399499deef690b))
* **deps:** bump minimum typing-extensions version ([3e87f77](https://github.com/CeramicTeam/ceramic-python/commit/3e87f77e5c0c9634b50520be6ebab2c8c60b5be7))
* **pydantic:** do not pass `by_alias` unless set ([8364d67](https://github.com/CeramicTeam/ceramic-python/commit/8364d673d495d7c8a0125c25254d6874bb039c0b))
* sanitize endpoint path params ([5daf5e7](https://github.com/CeramicTeam/ceramic-python/commit/5daf5e7c98dfe2820821b78a183b228d6a5b564c))
* update smoke test base_url to root ([e2233dd](https://github.com/CeramicTeam/ceramic-python/commit/e2233ddd3f7bf1248830380237836b368281196d))


### Chores

* **ci:** bump uv version ([60871ac](https://github.com/CeramicTeam/ceramic-python/commit/60871ac42a907812afad82470b3ab23f90a0c2fc))
* **ci:** skip lint on metadata-only changes ([b4f6bd0](https://github.com/CeramicTeam/ceramic-python/commit/b4f6bd05d70a54b82eee20f6633566702fae8dc0))
* **ci:** skip uploading artifacts on stainless-internal branches ([1f287c2](https://github.com/CeramicTeam/ceramic-python/commit/1f287c296d4a3111dea876b193982b479b96db5d))
* configure new SDK language ([4261901](https://github.com/CeramicTeam/ceramic-python/commit/4261901893e1dae44f75c5e3e8bf71986fcd8bad))
* format all `api.md` files ([57bcc3d](https://github.com/CeramicTeam/ceramic-python/commit/57bcc3db1497a14f3ac5f8caa674dc287b05758b))
* **internal:** add request options to SSE classes ([cf72d6b](https://github.com/CeramicTeam/ceramic-python/commit/cf72d6b830530e74cc91bd58114f1a0c15ab5be7))
* **internal:** make `test_proxy_environment_variables` more resilient ([8ac85d4](https://github.com/CeramicTeam/ceramic-python/commit/8ac85d46623e14a615d6c93eeeae800f8ab4c009))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([63e2792](https://github.com/CeramicTeam/ceramic-python/commit/63e279239128e71feff19b2e0e95b622a43d3349))
* **internal:** refactor authentication internals ([deddee4](https://github.com/CeramicTeam/ceramic-python/commit/deddee4053a01370b3eef87881fa1c1e34dd30fa))
* **internal:** remove mock server code ([3496061](https://github.com/CeramicTeam/ceramic-python/commit/3496061ed8380e1305386f44a0973aebffa58f2f))
* **internal:** tweak CI branches ([4cd9675](https://github.com/CeramicTeam/ceramic-python/commit/4cd96759c8e1a52c8e9b2f608912911312f4d1a7))
* **internal:** update gitignore ([63bfb19](https://github.com/CeramicTeam/ceramic-python/commit/63bfb19385f7901a1a352d93e76d717d28e513b2))
* update mock server docs ([facdb88](https://github.com/CeramicTeam/ceramic-python/commit/facdb88889325ad2a83b9f38d05743ca7eece792))


### Documentation

* add query param to README example request and include docs/support links in Stainless config ([a124d48](https://github.com/CeramicTeam/ceramic-python/commit/a124d483f176f5fed3d68198f130db8994c76a9c))
* fix python package name ([284cdc3](https://github.com/CeramicTeam/ceramic-python/commit/284cdc35cfb53e8c3c2dbddbedc1a0c577b45c59))
* staging branch version of OpenAPI spec ([0dab5c7](https://github.com/CeramicTeam/ceramic-python/commit/0dab5c79faca25b03f8b3ab24664a056763cab0b))
* update production repo ([e346f0d](https://github.com/CeramicTeam/ceramic-python/commit/e346f0dbada519dccaf30d7f2c8b99eca5a9c0ba))
* update README REST API documentation link to api-reference/search ([b33fe52](https://github.com/CeramicTeam/ceramic-python/commit/b33fe52eb1e1ff95aeea4813f8bf98356611f52a))
* updated error response ([c63b511](https://github.com/CeramicTeam/ceramic-python/commit/c63b5118c20bf73e5a74a5c8467998f110581144))

# System Dependencies

ExperimentsCloud uses external binaries through the Binary Discovery Framework.

## Resolution Order

1. Flask Configuration
2. Environment Variable
3. PATH
4. Raise BinaryNotFoundError

---

## Required

| Binary | Purpose |
|----------|---------|
| ffprobe | Video Metadata Extraction |
| ffmpeg | Video Processing & Test Generation |

---

## Verify

```bash
./scripts/check_system.sh
```

---

## Manual Verification

```bash
ffprobe -version
```

```bash
ffmpeg -version
```

---

## Override

```bash
export FFPROBE_BINARY=/path/to/ffprobe
```

```bash
export FFMPEG_BINARY=/path/to/ffmpeg
```

---

## Supported Platforms

- AlmaLinux
- Rocky Linux
- Fedora
- Ubuntu
- Debian
- Termux
- Docker
- CI/CD

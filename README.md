# Container Image Optimizer

Docker image optimization: multi-stage builds, layer analysis, vulnerability scanning.

## Features
- Layer cache hit analysis
- Auto-generate multi-stage Dockerfiles
- Base image recommendation (security + size)
- CVE vulnerability scanning

## Results
| Image | Before | After | Reduction |
|-------|--------|-------|----------|
| Python API | 1.2GB | 180MB | 85% |
| Node.js | 900MB | 120MB | 87% |

## License: MIT

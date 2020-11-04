Setup:

```
git clone https://github.com/llvm/llvm-project.git

sh launch_docker.sh

(docker): cd llvm-project

cmake -G Ninja ../llvm \
   -DLLVM_ENABLE_PROJECTS=mlir \
   -DLLVM_BUILD_EXAMPLES=ON \
   -DLLVM_TARGETS_TO_BUILD="X86;NVPTX;AMDGPU" \
   -DCMAKE_BUILD_TYPE=Release \
   -DLLVM_ENABLE_ASSERTIONS=ON

cmake --build . --target check-mlir

```

The docker container will be launched with 6GB of memory. This can be changed to the default 2GB. To check memory usage:
`docker ps -q | xargs  docker stats --no-stream`

Tutorial: https://mlir.llvm.org/docs/Tutorials/Toy/Ch-1/

Dockerfile: https://github.com/onnx/onnx-mlir

Talks: https://mlir.llvm.org/talks/

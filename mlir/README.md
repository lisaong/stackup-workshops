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

Tutorial: https://mlir.llvm.org/docs/Tutorials/Toy/Ch-1/

Dockerfile: https://github.com/onnx/onnx-mlir

Talks: https://mlir.llvm.org/talks/

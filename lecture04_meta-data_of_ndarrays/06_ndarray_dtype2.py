import numpy as np

int8_np = np.array([1,2,3], dtype=np.int8)
int16_np = np.array([1,2,3], dtype=np.int16)
int32_np = np.array([1,2,3], dtype=np.int32)
int64_np = np.array([1,2,3], dtype=np.int64)

uint8_np = np.array([1,2,3], dtype=np.uint8)
uint16_np = np.array([1,2,3], dtype=np.uint16)
uint32_np = np.array([1,2,3], dtype=np.uint32)
uint64_np = np.array([1,2,3], dtype=np.uint64)


float32_np = np.array([1,2,3], dtype=np.float32)
float64_np = np.array([1,2,3], dtype=np.float64)

print("Integer: {}/{}/{}/{}".format(int8_np.dtype, int16_np.dtype,
                                    int32_np.dtype, int64_np.dtype))
print("Unsigned Integer: {}/{}/{}/{}".format(uint8_np.dtype, uint16_np.dtype,
                                    uint32_np.dtype, uint64_np.dtype))
print("Floating Point: {}/{}".format(float32_np.dtype, float64_np.dtype))
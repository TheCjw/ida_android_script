__author__ = "TheCjw"

# the pointer of JavaVM object.
# JavaVM can be found at:
# -- JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM* vm, void* reserved);
# -- JNIEXPORT void JNICALL JNI_OnUnload(JavaVM* vm, void* reserved);
_JAVA_VM_OBJECT = 0x0000AB90

jni_names_list = ["jni_DestroyJavaVM",
                  "jni_AttachCurrentThread",
                  "jni_DetachCurrentThread",
                  "jni_GetEnv",
                  "jni_AttachCurrentThreadAsDaemon"]


def main():
    # Dword returns a long type value.
    table = Dword(_JAVA_VM_OBJECT)
    base = table + 0x4 * 3
    end = table + 0x4 * 8
    functions_list = [Dword(address) & 0xFFFFFFFFFFFFFFE for address in range(base, end, 4)]
    for i in xrange(0, len(jni_names_list)):
        MakeFunction(functions_list[i])
        MakeName(functions_list[i], jni_names_list[i])


if __name__ == "__main__":
    main()
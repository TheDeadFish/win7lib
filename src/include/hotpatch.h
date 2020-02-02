// Hotpatch V2.22, 11/01/2014
// DeadFish Shitware

#ifndef _HOTPATCH_H_
#define _HOTPATCH_H_

#ifdef __cplusplus
extern "C" {
#endif


#define HOTPATCH(old, new, pp) hotPatch((void*)old, (void*)new, (void**)pp)
#define HOTCALL(ftype, addr) (*((typeof(&ftype))((size_t)(addr))))
void hotPatch(void* lpOldProc, void* lpNewProc, void** lpPatchProc);

void hotPatch_static(void* lpPatchProc,
	void* lpOldProc, DWORD maxSize);
	

int hotPatch_instLen(void* ptr);
int hotPatch_getLen(BYTE* funcBase, int bytesNeeded);
void* hotPatch_getCall_(void* ptr);
void* hotPatch_getCall(void* ptr);

#ifdef __cplusplus
}
#endif

#endif

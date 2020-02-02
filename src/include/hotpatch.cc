// Hotpatch V2.25, 21/01/2015
// DeadFish Shitware

#include <windows.h>
#include <string.h>
#include "hotpatch.h"

#define SKIP 0x00
#define WROD 0x10
#define SEGM 0x20
#define REGM 0x30
#define IMPL 0x40
#define OFFS 0x50
#define GRP5 0x60
#define GRP3 0x70

static const char OneByte[] = {
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|IMPL, 1|IMPL, // 00
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|IMPL, 0|SKIP, // 08
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|IMPL, 1|IMPL, // 10
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|IMPL, 1|IMPL, // 18
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|SEGM, 1|IMPL, // 20
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|SEGM, 1|IMPL, // 28
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|SEGM, 1|IMPL, // 30
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 2|IMPL, 5|IMPL, 1|SEGM, 1|IMPL, // 38
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 40
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 48
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 50
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 58
	1|IMPL, 1|IMPL, 0|SKIP, 0|SKIP, 1|SEGM, 1|SEGM, 1|WROD, 0|SKIP, // 60
	5|IMPL, 5|REGM, 2|IMPL, 2|REGM, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 68
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, // 70
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, // 78
	2|REGM, 5|REGM, 0|SKIP, 2|REGM, 1|REGM, 1|REGM, 1|REGM, 1|REGM, // 80
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 0|SKIP, 1|REGM, 0|SKIP, 1|REGM, // 88
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // 90
	1|IMPL, 1|IMPL, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, // 98
	5|OFFS, 5|OFFS, 5|OFFS, 5|OFFS, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // A0
	2|IMPL, 5|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // A8
	2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, // B0
	5|IMPL, 5|IMPL, 5|IMPL, 5|IMPL, 5|IMPL, 5|IMPL, 5|IMPL, 5|IMPL, // B8
	2|REGM, 2|REGM, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 1|REGM, 5|REGM, // C0
	4|IMPL, 1|IMPL, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, // C8
	1|REGM, 1|REGM, 1|REGM, 1|REGM, 1|IMPL, 1|IMPL, 0|SKIP, 0|SKIP, // D0
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, // D8
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 2|IMPL, 2|IMPL, 2|IMPL, 2|IMPL, // E0
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, // E8
	0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 0|SKIP, 2|GRP3, 5|GRP3, // F0
	1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|IMPL, 1|REGM, 1|GRP5  // F8
}; 

int hotPatch_instLen(void* ptr)
{
	unsigned char* bptr =
		(unsigned char*)ptr;
	int length = 0;
	bool word = false;
	byte rex = 0;
	
	while(1)
	{
	#ifdef __x86_64__
		if((*bptr & 0xF0) == 0x40) {
			rex = *bptr++; continue; }
	#endif
		
		int opcode = OneByte[*bptr++];
		int regmem = *bptr;
		int size = opcode & 0x0F;
		int type = opcode & 0xF0;

		switch(type)
		{
		case SKIP:
			return -1;
		case WROD:
			word = true;
		case SEGM:
			length++;
			continue;
		case GRP3:
			if((regmem >> 3) & 7)
				size = 1;
			if(0){
		case GRP5:
			switch((regmem >> 3) & 7)
			{
			case 0:
			case 1:
			case 6:
				break;
			default:
				return -1;
			}}
		case REGM:
			switch(regmem >> 6)
			{
			case 0:
				length += 1;
				if((regmem & 7) == 4)
					length += 1;
				if((regmem & 7) == 5)
					length += 4;
				break;
			case 2:
				length += 3;
			case 1:
				length += 1;
				if((regmem & 7) == 4)
					length += 1;
			case 3:
				length += 1;
				break;
			}
		case IMPL:
			if(( size == 5 )
			&&( word == true))
				size = 3;
		case OFFS:
			length += size;
			break;
		}
		break;
	}
	return length;
}


class UnProtect
{
public:
	UnProtect(void* base, int length)
	{
		size_t funcBase = (size_t)base;
		pageBase = funcBase & ~4095;
		pageEnd = (funcBase+4095+length) & ~4095;
		VirtualProtect((PVOID)pageBase, pageEnd-pageBase,
			PAGE_EXECUTE_READWRITE, &flOldProtect);	
	}
	~UnProtect()
	{
		VirtualProtect((PVOID)pageBase, pageEnd-pageBase,
			flOldProtect, &flOldProtect);	
	}

private:
	size_t pageBase;
	size_t pageEnd;
	DWORD flOldProtect;
};

static
void hotPatchError()
{
	RaiseException(0xC0000001,
		EXCEPTION_NONCONTINUABLE, 0, NULL);
}

static
void hotPatch_makeJump(BYTE* src_, void* dst_)
{
	BYTE *src = (BYTE*)src_, *dst = (BYTE*)dst_;
	*src = 0xE9; *(int*)(src+1) = (dst-src)-5;
}

static 
void* hotPatch_getJump(void* ptr_)
{
	BYTE* ptr = (BYTE*)ptr_;
	return ptr+*(int*)(ptr+1)+5;
}

int hotPatch_getLen(BYTE* funcBase, int bytesNeeded)
{
	int bytesTaken = 0;
	while(bytesTaken < bytesNeeded)
	{
		int len = hotPatch_instLen(funcBase+bytesTaken);
		if(len < 0) return len;
		bytesTaken += len;
	}
	return bytesTaken;
}

void* hotPatch_getCall_(void* ptr_)
{
	BYTE* ptr = (BYTE*)ptr_;
	while(*ptr != 0xE8) { ptr += 
		hotPatch_instLen(ptr); }
	return ptr;
}

void* hotPatch_getCall(void* ptr)
{
	return hotPatch_getJump(
		hotPatch_getCall_(ptr));
}

void hotPatch_static(void* lpPatchProc,
	void* lpOldProc, DWORD maxSize)
{
	BYTE* funcBase = (BYTE*)(lpOldProc);
	int bytesTaken = hotPatch_getLen(funcBase, 5);
	if(bytesTaken > maxSize) hotPatchError();
	memcpy(lpPatchProc, funcBase, bytesTaken);
	hotPatch_makeJump((BYTE*)lpPatchProc+bytesTaken, funcBase+bytesTaken);
}


__attribute__((section(".hotPatch,\"xw\"#")))
static BYTE  hotPatch_data[4096];
static int hotPatch_size;

void* xheap_alloc(size_t size)
{
	int rem = sizeof(hotPatch_data)-hotPatch_size;
	if(rem < size) return NULL;
	void* p = hotPatch_data+hotPatch_size;
	hotPatch_size += size; return p;
}

void hotPatch(void* lpOldProc, void* lpNewProc, void** lpPatchProc)
{
	// check signature
	int bytesNeeded = 5;
	BYTE* funcBase = (BYTE*)(lpOldProc);
	if(memcmp(funcBase-5, "\x90\x90\x90\x90\x90", 5) == 0) {
		bytesNeeded = (*((WORD*)funcBase) != 0xFF8B) ? 2 : 0; }
	
	if( lpPatchProc != NULL )
	{
		// try and room for jump
		if(bytesNeeded == 0) {
			*lpPatchProc = (void*)(funcBase+2);
			goto PATCH_CODE; }
		
		int bytesTaken = hotPatch_getLen(
			funcBase, bytesNeeded);
		BYTE* pe = (BYTE*)xheap_alloc(bytesTaken+5);
		if(pe == NULL) hotPatchError();
		
		memcpy(pe, funcBase, bytesTaken);
		hotPatch_makeJump(pe+bytesTaken, 
			funcBase+bytesTaken);		
		*lpPatchProc = (void*)pe;
	}
	
	// Patch the code
PATCH_CODE:
	UnProtect unProtect(funcBase-5, 13);
	if(bytesNeeded != 5)
	{
		hotPatch_makeJump(funcBase-5, lpNewProc);
		*(WORD*)(funcBase) = 0xF9EB;
	}
	else
	{
		hotPatch_makeJump(funcBase, lpNewProc);
	}
}

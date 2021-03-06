#pragma once

// teb/peb access
#ifdef _M_AMD64
FORCEINLINE size_t NtReadTeb(size_t idx) { return __readgsqword(idx); }
#define NtWriteTeb(idx, value) __writegsdword(idx, value)
#else 
FORCEINLINE size_t NtReadTeb(size_t idx) { return __readfsdword(idx); }
#define NtWriteTeb(idx, value) __writefsdword(idx, value)
#endif
#undef NtCurrentPeb

__attribute__((const))
FORCEINLINE PPEB NtCurrentPeb(void) { return (PPEB)
	NtReadTeb(FIELD_OFFSET(TEB, ProcessEnvironmentBlock)); }
FORCEINLINE void SetWin32Err(DWORD err) {
	NtWriteTeb(FIELD_OFFSET(TEB, LastErrorValue), err); }
FORCEINLINE DWORD GetWin32Err(void) { return
	NtReadTeb(FIELD_OFFSET(TEB, LastErrorValue)); }
FORCEINLINE HANDLE BaseGetHeap(void) { 
	return NtCurrentPeb()->ProcessHeap; }

// heap allocation
static void WINAPI BaseFreeHeap(void* addr) { 
	RtlFreeHeap(BaseGetHeap(),0,addr); }
static void* WINAPI BaseAllocHeap(DWORD size) { 
	return RtlAllocateHeap(BaseGetHeap(),0,size); }

// pointer access
#define PB(x,i) (((char*)x)+(i))
#define PW(x,i) ((WORD*)PB(x,(i)))
#define PI(x,i) ((int*)PB(x,(i)))
#define RB(p,i) (*PB(p,i))
#define RW(p,i) (*PW(p,i))
#define RI(p,i) (*PI(p,i))

// retard compiler fixes
#define MEMFIX(x) asm volatile("" : "+m"(x))
#define VARFIX(x) asm volatile("" : "+g"(x))
#define CPYFIX(t,d,s) t d=s; VARFIX(d);
#define ZEROREG(x) asm volatile("xor %0,%0" : "+r"(x)); 
#define VARSET(x,y) { x=y; VARFIX(x); }

// 
#define XOR(d,m) ({ char z; asm("xor %2, %1" : "=@ccnz"(z), "+r"(d), "+r"(m)); z; })
#define AND(d,m) ({ char z; asm("and %2, %1" : "=@ccnz"(z), "+r"(d) : "g"(m)); z; })
#define INCP(s) asm("inc %0" : "+r"(s))	
#define MOVZX(d, s) asm("movzx %1, %0;" : "=r"(d) : "g"(s))
#define LDI_AND(d, s, m) { MOVZX(d, RB(s,0)); INCP(s); AND(d, m); }

// x86 string operations
#define STOSDN(p,v,n) for(int i = 0; i < 5; i++) STOSD(p,v);
#define STOSD(p,v) asm("stosl" : "+D"(p) : "a"((int)(v)) : "memory")

FORCEINLINE int isSingleBit(int x) { return !(x & (x-1)); }

// typedefs
typedef unsigned int u32;

// fast case insensitive compare
#define XORZ(dst, src) ({ char _ret_; asm("xor %2, %0" \
	: "+r"(dst), "=@ccz"(_ret_) : "g"(src)); _ret_; })
static inline int cmpiW(int ch1, int ch2) {
	return (XORZ(ch2, ch1) || (!(ch2 & -33)
		&& (u32)((ch1 &= -33)-65) < 26)); }
		
#define isSep(ch) ((ch == '\\')||(ch == '/'))


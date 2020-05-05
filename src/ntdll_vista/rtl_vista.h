/*
 * COPYRIGHT:       See COPYING in the top level directory
 * PROJECT:         ReactOS System Libraries
 * FILE:            lib/rtl/rtl.h
 * PURPOSE:         Run-Time Libary Header
 * PROGRAMMER:      Alex Ionescu
 */

#ifndef RTL_H
#define RTL_H

/* We're a core NT DLL, we don't import syscalls */
#define _INC_SWPRINTF_INL_
#undef __MSVCRT__

/* C Headers */
#include <stdlib.h>
#include <stdio.h>

/* PSDK/NDK Headers */
//#define WIN32_NO_STATUS
//#define _INC_WINDOWS
//#define COM_NO_WINDOWS_H
//#define COBJMACROS
//#define CONST_VTABLE
#include <windef.h>
#include <winbase.h>
#include <winreg.h>
#include <objbase.h>
//#include <ntintsafe.h>
#include <ndk/ntndk.h>

/* SEH support with PSEH */
//#include <pseh/pseh2.h>

/* Use intrinsics for x86 and x64 */
#if defined(_M_IX86) || defined(_M_AMD64)
#define InterlockedCompareExchange _InterlockedCompareExchange
#define InterlockedIncrement _InterlockedIncrement
#define InterlockedDecrement _InterlockedDecrement
#define InterlockedExchangeAdd _InterlockedExchangeAdd
#define InterlockedExchange _InterlockedExchange
#define InterlockedBitTestAndSet _interlockedbittestandset
#define InterlockedBitTestAndSet64 _interlockedbittestandset64
#endif

/* mingw-w64 fixes */
#define InterlockedAdd64 _InterlockedAdd64
#define InterlockedAnd64 _InterlockedAnd64
#define InterlockedOr64 _InterlockedOr64
#define InterlockedAdd _InterlockedAdd
#define InterlockedAnd _InterlockedAnd
#define InterlockedOr _InterlockedOr

#include <intrin.h>

/* wine stuff */
#define FIXME(...)
#define TRACE(...)

#endif /* RTL_H */

#include "k32_vista.h"

#define ERROR_OBJECT_NAME_EXISTS 698

struct proc_thread_attr
{
    DWORD_PTR attr;
    SIZE_T size;
    void *value;
};

struct _PROC_THREAD_ATTRIBUTE_LIST
{
    DWORD mask;  /* bitmask of items in list */
    DWORD size;  /* max number of items in list */
    DWORD count; /* number of items in list */
    DWORD pad;
    DWORD_PTR unk;
    struct proc_thread_attr attrs[1];
};

/***********************************************************************
 *           InitializeProcThreadAttributeList       (KERNEL32.@)
 */
BOOL WINAPI InitializeProcThreadAttributeList(struct _PROC_THREAD_ATTRIBUTE_LIST *list,
                                              DWORD count, DWORD flags, SIZE_T *size)
{
    SIZE_T needed;
    BOOL ret = FALSE;

    TRACE("(%p %d %x %p)\n", list, count, flags, size);

    needed = FIELD_OFFSET(struct _PROC_THREAD_ATTRIBUTE_LIST, attrs[count]);
    if (list && *size >= needed)
    {
        list->mask = 0;
        list->size = count;
        list->count = 0;
        list->unk = 0;
        ret = TRUE;
    }
    else
        SetLastError(ERROR_INSUFFICIENT_BUFFER);

    *size = needed;
    return ret;
}

/***********************************************************************
 *           UpdateProcThreadAttribute       (KERNEL32.@)
 */
BOOL WINAPI UpdateProcThreadAttribute(struct _PROC_THREAD_ATTRIBUTE_LIST *list,
                                      DWORD flags, DWORD_PTR attr, void *value, SIZE_T size,
                                      void *prev_ret, SIZE_T *size_ret)
{
    DWORD mask;
    struct proc_thread_attr *entry;

    TRACE("(%p %x %08lx %p %ld %p %p)\n", list, flags, attr, value, size, prev_ret, size_ret);

    if (list->count >= list->size)
    {
        SetLastError(ERROR_GEN_FAILURE);
        return FALSE;
    }

    switch (attr)
    {
    case PROC_THREAD_ATTRIBUTE_PARENT_PROCESS:
        if (size != sizeof(HANDLE))
        {
            SetLastError(ERROR_BAD_LENGTH);
            return FALSE;
        }
        break;

    case PROC_THREAD_ATTRIBUTE_HANDLE_LIST:
        if ((size / sizeof(HANDLE)) * sizeof(HANDLE) != size)
        {
            SetLastError(ERROR_BAD_LENGTH);
            return FALSE;
        }
        break;

    case PROC_THREAD_ATTRIBUTE_IDEAL_PROCESSOR:
        if (size != sizeof(PROCESSOR_NUMBER))
        {
            SetLastError(ERROR_BAD_LENGTH);
            return FALSE;
        }
        break;

	/*
    case PROC_THREAD_ATTRIBUTE_CHILD_PROCESS_POLICY:
       if (size != sizeof(DWORD) && size != sizeof(DWORD64))
       {
           SetLastError(ERROR_BAD_LENGTH);
           return FALSE;
       }
       break;

    case PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY:
        if (size != sizeof(DWORD) && size != sizeof(DWORD64) && size != sizeof(DWORD64) * 2)
        {
            SetLastError(ERROR_BAD_LENGTH);
            return FALSE;
        }
        break;
		*/

    default:
        SetLastError(ERROR_NOT_SUPPORTED);
        FIXME("Unhandled attribute number %lu\n", attr & PROC_THREAD_ATTRIBUTE_NUMBER);
        return FALSE;
    }

    mask = 1 << (attr & PROC_THREAD_ATTRIBUTE_NUMBER);

    if (list->mask & mask)
    {
        SetLastError(ERROR_OBJECT_NAME_EXISTS);
        return FALSE;
    }

    list->mask |= mask;

    entry = list->attrs + list->count;
    entry->attr = attr;
    entry->size = size;
    entry->value = value;
    list->count++;

    return TRUE;
}

/***********************************************************************
 *           DeleteProcThreadAttributeList       (KERNEL32.@)
 */
void WINAPI DeleteProcThreadAttributeList(struct _PROC_THREAD_ATTRIBUTE_LIST *list)
{
    return;
}


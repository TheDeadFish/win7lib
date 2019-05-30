#include "iphlpapi.h"

/******************************************************************
 *    ConvertInterfaceIndexToLuid (IPHLPAPI.@)
 */
DWORD WINAPI ConvertInterfaceIndexToLuid(NET_IFINDEX index, NET_LUID *luid)
{
    MIB_IFROW row;

    TRACE("(%u %p)\n", index, luid);

    if (!luid) return ERROR_INVALID_PARAMETER;
    memset( luid, 0, sizeof(*luid) );

    row.dwIndex = index;
    if (GetIfEntry( &row )) return ERROR_FILE_NOT_FOUND;

    luid->Info.Reserved     = 0;
    luid->Info.NetLuidIndex = index;
    luid->Info.IfType       = row.dwType;
    return NO_ERROR;
}

/******************************************************************
 *    ConvertInterfaceLuidToNameW (IPHLPAPI.@)
 */
DWORD WINAPI ConvertInterfaceLuidToNameW(const NET_LUID *luid, WCHAR *name, SIZE_T len)
{
    DWORD ret;
    MIB_IFROW row;

    TRACE("(%p %p %u)\n", luid, name, (DWORD)len);

    if (!luid || !name) return ERROR_INVALID_PARAMETER;

    row.dwIndex = luid->Info.NetLuidIndex;
    if ((ret = GetIfEntry( &row ))) return ret;

    if (len < strlenW( row.wszName ) + 1) return ERROR_NOT_ENOUGH_MEMORY;
    strcpyW( name, row.wszName );
    return NO_ERROR;
}

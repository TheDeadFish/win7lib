#include "user32_vista.h"

/**********************************************************************
 * RegisterPowerSettingNotification [USER32.@]
 */
HPOWERNOTIFY WINAPI RegisterPowerSettingNotification(HANDLE recipient, const GUID *guid, DWORD flags)
{
    FIXME("(%p,%s,%x): stub\n", recipient, debugstr_guid(guid), flags);
    return (HPOWERNOTIFY)0xdeadbeef;
}

/**********************************************************************
 * UnregisterPowerSettingNotification [USER32.@]
 */
BOOL WINAPI UnregisterPowerSettingNotification(HPOWERNOTIFY handle)
{
    FIXME("(%p): stub\n", handle);
    return TRUE;
}

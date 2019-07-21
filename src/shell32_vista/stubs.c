#include <windows.h>
#define FIXME(...)

/*************************************************************************
 * SHGetPropertyStoreForWindow [SHELL32.@]
 */
HRESULT WINAPI SetCurrentProcessExplicitAppUserModelID(const WCHAR *appid)
{
    FIXME("%s: stub\n", debugstr_w(appid));
    return E_NOTIMPL;
}

/*************************************************************************
 * SHGetPropertyStoreForWindow [SHELL32.@]
 */
HRESULT WINAPI SHGetPropertyStoreForWindow(HWND hwnd, REFIID riid, void **ppv)
{
    FIXME("(%p %p %p) stub!\n", hwnd, riid, ppv);
    return E_NOTIMPL;
}

/***********************************************************************
 *              SHQueryUserNotificationState (SHELL32.@)
 */
HRESULT WINAPI SHQueryUserNotificationState(QUERY_USER_NOTIFICATION_STATE *state)
{
    FIXME("%p: stub\n", state);
    *state = QUNS_ACCEPTS_NOTIFICATIONS;
    return S_OK;
}

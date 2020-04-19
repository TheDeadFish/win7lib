#include <windows.h>
#include <stdio.h>
#include <string.h>

void fatal_error(const char*fmt,...) {
	va_list args; va_start (args, fmt);
	vfprintf(stderr, fmt,args);
	exit(1); va_end (args); }
	
static 
LCID LCIDmapDefault(LCID lcid)
{
	if(lcid == LOCALE_SYSTEM_DEFAULT)
		return GetSystemDefaultLCID();
	if((lcid & ~0xC00) == 0)
		return GetUserDefaultLCID();
	return lcid;
}
	

typedef struct
{
	WCHAR name[24];
	int lcid, link;
}LocalInfo_t;


LocalInfo_t localList[4096];
int nLocale = 0;


void print_locale(LocalInfo_t* li)
{
	char tmp[128];
	int len = sprintf(tmp, "\t[\"%S\",", li->name);
	while(len < 11) tmp[len++] = ' ';
	if(li->lcid > 0xFFFF) { len += sprintf(tmp+len, "0x%08x", li->lcid); }
	else { len += sprintf(tmp+len, "0x%04x", li->lcid); }
	if(li->lcid != li->link) len += sprintf(tmp+len, ", 0x%04x", li->link);
	printf("%.*s],\n", len, tmp);
}

int main(int argc, char* argv[])
{
	// specials
	int userDefault = LocaleNameToLCID(NULL, 0);
	int sysDefault = LocaleNameToLCID(L"!x-sys-default-locale", 0);
	if((userDefault != GetUserDefaultLCID())
	||(sysDefault != GetSystemDefaultLCID()))
		printf("default: %X, %X\n", userDefault, sysDefault);

	for(int i = 0; i < 0x60000; i++)
	{ 
		// get local name and link
		LocalInfo_t* li = &localList[nLocale]; li->name[0] = 0;
		int len = LCIDToLocaleName(i, li->name, 24, LOCALE_ALLOW_NEUTRAL_NAMES);
		int link = LocaleNameToLCID(localList[nLocale].name, 0);
		
		// en-US (special case)
		if((i & ~0xC00) == 0) {
			if(link != LCIDmapDefault(i))
				fatal_error("default: %d, %d", i, link); 
			continue;
		}
		
		// insert into list
		if(len) { li->lcid = i; 
			li->link = link; nLocale++;
			if(argv[1]) print_locale(li);
		}
	}
	
	// check lcid and link
	WCHAR buff[24];
	for(int i = 0; i < nLocale; i++) {
		LocalInfo_t* li = &localList[i]; 
		
		// check lcid
		int lcid = LocaleNameToLCID(li->name, LOCALE_ALLOW_NEUTRAL_NAMES);
		if(lcid != li->lcid) fatal_error("name->lcid: %d, %d, %S",
			lcid, li->lcid, li->name);
			
		// check link name
		buff[0] = 0;	
		LCIDToLocaleName(lcid, buff, 24, 0);
		for(int j = 0; j < nLocale; j++) {
			if((localList[j].lcid == li->link)
			&&(!wcscmp(localList[j].name, buff)))
				goto FOUND_LINK;
		}
		
		fatal_error("lcid->name: %d, %S, %S",	
			lcid, li->name, buff);
	FOUND_LINK:;
	}
}

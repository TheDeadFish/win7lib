#include <stdshit.h>
#include "peFile/peFile.h"
const char progName[] = "ntv6-patch";

typedef cch* map_t[2];


const map_t dll_map[] = {
	{"ntdll.dll", "ntdllex.dll"},
	{"kernel32.dll", "krnl32ex.dll"},
	{"shell32.dll", "shellex.dll"},
	{"KERNELBASE.dll", "krnl32ex.dll"},
	{"API-MS-Win-Core", "krnl32ex.dll"},
	{"msvcrt.dll", "msvcrx.dll"},
	{NULL, NULL}
};

int import_fix(const map_t* dll_map, PeFile& peFile)
{
	peFile.boundImp.Clear();
	
	u32 impRva = peFile.dataDir(peFile.IDE_IMPORT).rva;
	if(!impRva) return 0; 
	while(1) {	
		IMAGE_IMPORT_DESCRIPTOR* impDesc = peFile.rvaToPtr(
			impRva, sizeof(IMAGE_IMPORT_DESCRIPTOR));
		if(!impDesc) return 1; if(!impDesc->Name) return 0;
		impRva += sizeof(IMAGE_IMPORT_DESCRIPTOR);
		auto dllName = peFile.chkStr2(impDesc->Name);
		if(!dllName) return 2;
		
		for(auto x = dll_map; (*x)[0]; x++) {
			if(strSicmp(dllName.data, (*x)[0])) {
				strcpy((char*)dllName.data, (*x)[1]);
				break;
			}
		}
	}
	
	return 0;
}


cch* do_patch(cch* srcFile, cch* dstFile)
{
	PeFile peFile;
	IFRET(peFile.load(srcFile));
		
	// set win version
	peFile.Win32VersionValue = 0x106;
	peFile.MajorOperatingSystemVersion = 5;
	peFile.MajorSubsystemVersion = 5;
	
	// fix import directory
	if(import_fix(dll_map, peFile))
		return "bad imports";
	
	if(peFile.save(dstFile))
		return "save error";
	return NULL;
}


int main(int argc, char** argv)
{
	if(argc < 2) { fatalError(NULL, "ntv6-patch: <file>\n"); }
	for(int i = 1; i < argc; i++) {
		cch* err = do_patch(argv[i],argv[i]);
		if(err) contError(NULL, err);
	}
}

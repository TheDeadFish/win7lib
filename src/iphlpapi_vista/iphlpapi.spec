@ stdcall AddIPAddress( long long long ptr ptr ) IPHLPAPI.AddIPAddress
@ stub AllocateAndGetArpEntTableFromStack IPHLPAPI.AllocateAndGetArpEntTableFromStack
@ stdcall AllocateAndGetIfTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetIfTableFromStack
@ stdcall AllocateAndGetIpAddrTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetIpAddrTableFromStack
@ stdcall AllocateAndGetIpForwardTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetIpForwardTableFromStack
@ stdcall AllocateAndGetIpNetTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetIpNetTableFromStack
@ stdcall AllocateAndGetTcpExTable2FromStack( ptr long long long long long ) IPHLPAPI.AllocateAndGetTcpExTable2FromStack
@ stdcall AllocateAndGetTcpExTableFromStack( ptr long long long long ) IPHLPAPI.AllocateAndGetTcpExTableFromStack
@ stdcall AllocateAndGetTcpTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetTcpTableFromStack
@ stdcall AllocateAndGetUdpExTable2FromStack( ptr long long long long long ) IPHLPAPI.AllocateAndGetUdpExTable2FromStack
@ stdcall AllocateAndGetUdpExTableFromStack( ptr long long long long ) IPHLPAPI.AllocateAndGetUdpExTableFromStack
@ stdcall AllocateAndGetUdpTableFromStack( ptr long long long ) IPHLPAPI.AllocateAndGetUdpTableFromStack
@ stdcall CancelIPChangeNotify(ptr) IPHLPAPI.CancelIPChangeNotify
@ stub CancelSecurityHealthChangeNotify IPHLPAPI.CancelSecurityHealthChangeNotify
@ stdcall CreateIpForwardEntry( ptr ) IPHLPAPI.CreateIpForwardEntry
@ stdcall CreateIpNetEntry( ptr ) IPHLPAPI.CreateIpNetEntry
@ stdcall CreateProxyArpEntry( long long long ) IPHLPAPI.CreateProxyArpEntry
@ stdcall DeleteIPAddress( long ) IPHLPAPI.DeleteIPAddress
@ stdcall DeleteIpForwardEntry( ptr ) IPHLPAPI.DeleteIpForwardEntry
@ stdcall DeleteIpNetEntry( ptr ) IPHLPAPI.DeleteIpNetEntry
@ stdcall DeleteProxyArpEntry( long long long ) IPHLPAPI.DeleteProxyArpEntry
@ stdcall DisableMediaSense(ptr ptr) IPHLPAPI.DisableMediaSense
@ stdcall EnableRouter( ptr ptr ) IPHLPAPI.EnableRouter
@ stdcall FlushIpNetTable( long ) IPHLPAPI.FlushIpNetTable
@ stub FlushIpNetTableFromStack IPHLPAPI.FlushIpNetTableFromStack
@ stdcall GetAdapterIndex( wstr ptr ) IPHLPAPI.GetAdapterIndex
@ stdcall GetAdapterOrderMap() IPHLPAPI.GetAdapterOrderMap
@ stdcall GetAdaptersAddresses( long long ptr ptr ptr ) IPHLPAPI.GetAdaptersAddresses
@ stdcall GetAdaptersInfo( ptr ptr ) IPHLPAPI.GetAdaptersInfo
@ stdcall GetBestInterface( long ptr ) IPHLPAPI.GetBestInterface
@ stdcall GetBestInterfaceEx(ptr ptr) IPHLPAPI.GetBestInterfaceEx
@ stub GetBestInterfaceFromStack IPHLPAPI.GetBestInterfaceFromStack
@ stdcall GetBestRoute( long long long ) IPHLPAPI.GetBestRoute
@ stub GetBestRouteFromStack IPHLPAPI.GetBestRouteFromStack
@ stdcall GetExtendedTcpTable( ptr ptr long long long long ) IPHLPAPI.GetExtendedTcpTable
@ stdcall GetExtendedUdpTable( ptr ptr long long long long ) IPHLPAPI.GetExtendedUdpTable
@ stdcall GetFriendlyIfIndex( long ) IPHLPAPI.GetFriendlyIfIndex
@ stdcall GetIcmpStatistics( ptr ) IPHLPAPI.GetIcmpStatistics
@ stdcall GetIcmpStatisticsEx(ptr long) IPHLPAPI.GetIcmpStatisticsEx
@ stub GetIcmpStatsFromStack IPHLPAPI.GetIcmpStatsFromStack
@ stub GetIcmpStatsFromStackEx IPHLPAPI.GetIcmpStatsFromStackEx
@ stdcall GetIfEntry( ptr ) IPHLPAPI.GetIfEntry
@ stub GetIfEntryFromStack IPHLPAPI.GetIfEntryFromStack
@ stdcall GetIfTable( ptr ptr long ) IPHLPAPI.GetIfTable
@ stub GetIfTableFromStack IPHLPAPI.GetIfTableFromStack
@ stub GetIgmpList IPHLPAPI.GetIgmpList
@ stdcall GetInterfaceInfo( ptr ptr ) IPHLPAPI.GetInterfaceInfo
@ stdcall GetIpAddrTable( ptr ptr long ) IPHLPAPI.GetIpAddrTable
@ stub GetIpAddrTableFromStack IPHLPAPI.GetIpAddrTableFromStack
@ stdcall GetIpErrorString(long ptr ptr) IPHLPAPI.GetIpErrorString
@ stdcall GetIpForwardTable( ptr ptr long ) IPHLPAPI.GetIpForwardTable
@ stub GetIpForwardTableFromStack IPHLPAPI.GetIpForwardTableFromStack
@ stdcall GetIpNetTable( ptr ptr long ) IPHLPAPI.GetIpNetTable
@ stub GetIpNetTableFromStack IPHLPAPI.GetIpNetTableFromStack
@ stdcall GetIpStatistics( ptr ) IPHLPAPI.GetIpStatistics
@ stdcall GetIpStatisticsEx(ptr long) IPHLPAPI.GetIpStatisticsEx
@ stub GetIpStatsFromStack IPHLPAPI.GetIpStatsFromStack
@ stub GetIpStatsFromStackEx IPHLPAPI.GetIpStatsFromStackEx
@ stdcall GetNetworkParams( ptr ptr ) IPHLPAPI.GetNetworkParams
@ stdcall GetNumberOfInterfaces( ptr ) IPHLPAPI.GetNumberOfInterfaces
@ stub GetOwnerModuleFromTcp6Entry IPHLPAPI.GetOwnerModuleFromTcp6Entry
@ stdcall GetOwnerModuleFromTcpEntry ( ptr long ptr ptr ) IPHLPAPI.GetOwnerModuleFromTcpEntry
@ stub GetOwnerModuleFromUdp6Entry IPHLPAPI.GetOwnerModuleFromUdp6Entry
@ stdcall GetOwnerModuleFromUdpEntry ( ptr long ptr ptr ) IPHLPAPI.GetOwnerModuleFromUdpEntry
@ stdcall GetPerAdapterInfo( long ptr ptr ) IPHLPAPI.GetPerAdapterInfo
@ stdcall GetRTTAndHopCount( long ptr long ptr ) IPHLPAPI.GetRTTAndHopCount
@ stub GetTcpExTable2FromStack IPHLPAPI.GetTcpExTable2FromStack
@ stdcall GetTcpStatistics( ptr ) IPHLPAPI.GetTcpStatistics
@ stdcall GetTcpStatisticsEx(ptr long) IPHLPAPI.GetTcpStatisticsEx
@ stub GetTcpStatsFromStack IPHLPAPI.GetTcpStatsFromStack
@ stub GetTcpStatsFromStackEx IPHLPAPI.GetTcpStatsFromStackEx
@ stdcall GetTcpTable( ptr ptr long ) IPHLPAPI.GetTcpTable
@ stub GetTcpTableFromStack IPHLPAPI.GetTcpTableFromStack
@ stub GetUdpExTable2FromStack IPHLPAPI.GetUdpExTable2FromStack
@ stdcall GetUdpStatistics( ptr ) IPHLPAPI.GetUdpStatistics
@ stdcall GetUdpStatisticsEx(ptr long) IPHLPAPI.GetUdpStatisticsEx
@ stub GetUdpStatsFromStack IPHLPAPI.GetUdpStatsFromStack
@ stub  GetUdpStatsFromStackEx IPHLPAPI.GetUdpStatsFromStackEx
@ stdcall GetUdpTable( ptr ptr long ) IPHLPAPI.GetUdpTable
@ stub GetUdpTableFromStack IPHLPAPI.GetUdpTableFromStack
@ stdcall GetUniDirectionalAdapterInfo( ptr ptr ) IPHLPAPI.GetUniDirectionalAdapterInfo
@ stdcall Icmp6CreateFile() IPHLPAPI.Icmp6CreateFile
@ stdcall Icmp6ParseReplies(ptr long) IPHLPAPI.Icmp6ParseReplies
@ stdcall Icmp6SendEcho2(ptr ptr ptr ptr ptr ptr ptr long ptr ptr long long) IPHLPAPI.Icmp6SendEcho2
@ stdcall IcmpCloseHandle(ptr) IPHLPAPI.IcmpCloseHandle
@ stdcall IcmpCreateFile() IPHLPAPI.IcmpCreateFile
@ stdcall IcmpParseReplies(ptr long) IPHLPAPI.IcmpParseReplies
@ stdcall IcmpSendEcho2(ptr ptr ptr ptr long ptr long ptr ptr long long) IPHLPAPI.IcmpSendEcho2
@ stdcall IcmpSendEcho(ptr long ptr long ptr ptr long long) IPHLPAPI.IcmpSendEcho
@ stub InternalCreateIpForwardEntry IPHLPAPI.InternalCreateIpForwardEntry
@ stub InternalCreateIpNetEntry IPHLPAPI.InternalCreateIpNetEntry
@ stub InternalDeleteIpForwardEntry IPHLPAPI.InternalDeleteIpForwardEntry
@ stub InternalDeleteIpNetEntry IPHLPAPI.InternalDeleteIpNetEntry
@ stub InternalGetIfTable IPHLPAPI.InternalGetIfTable
@ stub InternalGetIpAddrTable IPHLPAPI.InternalGetIpAddrTable
@ stub InternalGetIpForwardTable IPHLPAPI.InternalGetIpForwardTable
@ stub InternalGetIpNetTable IPHLPAPI.InternalGetIpNetTable
@ stub InternalGetTcpTable IPHLPAPI.InternalGetTcpTable
@ stub InternalGetUdpTable IPHLPAPI.InternalGetUdpTable
@ stub InternalSetIfEntry IPHLPAPI.InternalSetIfEntry
@ stub InternalSetIpForwardEntry IPHLPAPI.InternalSetIpForwardEntry
@ stub InternalSetIpNetEntry IPHLPAPI.InternalSetIpNetEntry
@ stub InternalSetIpStats IPHLPAPI.InternalSetIpStats
@ stub InternalSetTcpEntry IPHLPAPI.InternalSetTcpEntry
@ stdcall IpReleaseAddress( ptr ) IPHLPAPI.IpReleaseAddress
@ stdcall IpRenewAddress( ptr ) IPHLPAPI.IpRenewAddress
@ stub IsLocalAddress IPHLPAPI.IsLocalAddress
@ stub NTPTimeToNTFileTime IPHLPAPI.NTPTimeToNTFileTime
@ stub NTTimeToNTPTime IPHLPAPI.NTTimeToNTPTime
@ stub NhGetGuidFromInterfaceName IPHLPAPI.NhGetGuidFromInterfaceName
@ stdcall NhGetInterfaceNameFromDeviceGuid(ptr ptr ptr long long) IPHLPAPI.NhGetInterfaceNameFromDeviceGuid
@ stdcall NhGetInterfaceNameFromGuid(ptr ptr ptr long long) IPHLPAPI.NhGetInterfaceNameFromGuid
@ stdcall NhpAllocateAndGetInterfaceInfoFromStack(ptr ptr long ptr long) IPHLPAPI.NhpAllocateAndGetInterfaceInfoFromStack
@ stub NhpGetInterfaceIndexFromStack IPHLPAPI.NhpGetInterfaceIndexFromStack
@ stdcall NotifyAddrChange( ptr ptr ) IPHLPAPI.NotifyAddrChange
@ stdcall NotifyRouteChange( ptr ptr ) IPHLPAPI.NotifyRouteChange
@ stub NotifyRouteChangeEx IPHLPAPI.NotifyRouteChangeEx
@ stub NotifySecurityHealthChange IPHLPAPI.NotifySecurityHealthChange
@ stdcall RestoreMediaSense(ptr ptr) IPHLPAPI.RestoreMediaSense
@ stdcall SendARP(long long ptr ptr) IPHLPAPI.SendARP
@ stub SetAdapterIpAddress IPHLPAPI.SetAdapterIpAddress
@ stub SetBlockRoutes IPHLPAPI.SetBlockRoutes
@ stdcall SetIfEntry( ptr ) IPHLPAPI.SetIfEntry
@ stub SetIfEntryToStack IPHLPAPI.SetIfEntryToStack
@ stdcall SetIpForwardEntry( ptr ) IPHLPAPI.SetIpForwardEntry
@ stdcall SetIpForwardEntryToStack( ptr ) IPHLPAPI.SetIpForwardEntryToStack
@ stub SetIpMultihopRouteEntryToStack IPHLPAPI.SetIpMultihopRouteEntryToStack
@ stdcall SetIpNetEntry( ptr ) IPHLPAPI.SetIpNetEntry
@ stub SetIpNetEntryToStack IPHLPAPI.SetIpNetEntryToStack
@ stub SetIpRouteEntryToStack IPHLPAPI.SetIpRouteEntryToStack
@ stdcall SetIpStatistics( ptr ) IPHLPAPI.SetIpStatistics
@ stub SetIpStatsToStack IPHLPAPI.SetIpStatsToStack
@ stdcall SetIpTTL( long ) IPHLPAPI.SetIpTTL
@ stub SetProxyArpEntryToStack IPHLPAPI.SetProxyArpEntryToStack
@ stub SetRouteWithRef IPHLPAPI.SetRouteWithRef
@ stdcall SetTcpEntry( ptr ) IPHLPAPI.SetTcpEntry
@ stub SetTcpEntryToStack IPHLPAPI.SetTcpEntryToStack
@ stdcall UnenableRouter( ptr ptr ) IPHLPAPI.UnenableRouter
@ stdcall -arch=i386 _PfAddFiltersToInterface@24() _PfAddFiltersToInterface@24
@ stdcall -arch=i386 _PfAddGlobalFilterToInterface@8() _PfAddGlobalFilterToInterface@8
@ stdcall -arch=i386 _PfBindInterfaceToIPAddress@12() _PfBindInterfaceToIPAddress@12
@ stdcall -arch=i386 _PfBindInterfaceToIndex@16() _PfBindInterfaceToIndex@16
@ stdcall -arch=i386 _PfCreateInterface@24() _PfCreateInterface@24
@ stdcall -arch=i386 _PfDeleteInterface@4() _PfDeleteInterface@4
@ stdcall -arch=i386 _PfDeleteLog@0() _PfDeleteLog@0
@ stdcall -arch=i386 _PfGetInterfaceStatistics@16() _PfGetInterfaceStatistics@16
@ stdcall -arch=i386 _PfMakeLog@4() _PfMakeLog@4
@ stdcall -arch=i386 _PfRebindFilters@8() _PfRebindFilters@8
@ stdcall -arch=i386 _PfRemoveFilterHandles@12() _PfRemoveFilterHandles@12
@ stdcall -arch=i386 _PfRemoveFiltersFromInterface@20() _PfRemoveFiltersFromInterface@20
@ stdcall -arch=i386 _PfRemoveGlobalFilterFromInterface@8() _PfRemoveGlobalFilterFromInterface@8
@ stdcall -arch=i386 _PfSetLogBuffer@28() _PfSetLogBuffer@28
@ stdcall -arch=i386 _PfTestPacket@20() _PfTestPacket@20
@ stdcall -arch=i386 _PfUnBindInterface@4() _PfUnBindInterface@4
@ stdcall -arch=x86_64 _PfAddFiltersToInterface@24() IPHLPAPI._PfAddFiltersToInterface@24
@ stdcall -arch=x86_64 _PfAddGlobalFilterToInterface@8() IPHLPAPI._PfAddGlobalFilterToInterface@8
@ stdcall -arch=x86_64 _PfBindInterfaceToIPAddress@12() IPHLPAPI._PfBindInterfaceToIPAddress@12
@ stdcall -arch=x86_64 _PfBindInterfaceToIndex@16() IPHLPAPI._PfBindInterfaceToIndex@16
@ stdcall -arch=x86_64 _PfCreateInterface@24() IPHLPAPI._PfCreateInterface@24
@ stdcall -arch=x86_64 _PfDeleteInterface@4() IPHLPAPI._PfDeleteInterface@4
@ stdcall -arch=x86_64 _PfDeleteLog@0() IPHLPAPI._PfDeleteLog@0
@ stdcall -arch=x86_64 _PfGetInterfaceStatistics@16() IPHLPAPI._PfGetInterfaceStatistics@16
@ stdcall -arch=x86_64 _PfMakeLog@4() IPHLPAPI._PfMakeLog@4
@ stdcall -arch=x86_64 _PfRebindFilters@8() IPHLPAPI._PfRebindFilters@8
@ stdcall -arch=x86_64 _PfRemoveFilterHandles@12() IPHLPAPI._PfRemoveFilterHandles@12
@ stdcall -arch=x86_64 _PfRemoveFiltersFromInterface@20() IPHLPAPI._PfRemoveFiltersFromInterface@20
@ stdcall -arch=x86_64 _PfRemoveGlobalFilterFromInterface@8() IPHLPAPI._PfRemoveGlobalFilterFromInterface@8
@ stdcall -arch=x86_64 _PfSetLogBuffer@28() IPHLPAPI._PfSetLogBuffer@28
@ stdcall -arch=x86_64 _PfTestPacket@20() IPHLPAPI._PfTestPacket@20
@ stdcall -arch=x86_64 _PfUnBindInterface@4() IPHLPAPI._PfUnBindInterface@4
@ stub do_echo_rep IPHLPAPI.do_echo_rep
@ stub do_echo_req IPHLPAPI.do_echo_req
@ stub register_icmp IPHLPAPI.register_icmp

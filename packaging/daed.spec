%global debug_package %{nil}

%{!?daed_version:%global daed_version 2.2.0}
%{!?release_base:%global release_base 10}
%{!?site_tag:%global site_tag 0}
%{!?ip_tag:%global ip_tag 0}

Name:           daed
Version:        %{daed_version}
Release:        %{release_base}.%{site_tag}.%{ip_tag}%{?dist}
Summary:        daed, a modern dashboard with dae.

License:        MIT
URL:            https://github.com/daeuniverse/daed

Source0:        daed
Source1:        daed.service
Source2:        LICENSE
Source10:       geosite.dat
Source11:       geoip.dat

BuildRequires:  systemd-rpm-macros
Requires:       glibc

%description
%{summary} With newer dae backend for extended BPF header support.

%prep

%build

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/daed
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/daed.service

install -Dm644 %{SOURCE2} %{buildroot}%{_licensedir}/%{name}/LICENSE

install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/daed/geosite.dat
install -Dm644 %{SOURCE11} %{buildroot}%{_datadir}/daed/geoip.dat


%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/daed
%{_unitdir}/daed.service
%{_datadir}/daed/geoip.dat
%{_datadir}/daed/geosite.dat



%changelog
* Tue Sep 29 2026 D3adEr1c <lqyyy0717@outlook.com> - 2.2.0
- Sync upstream daed 2.1.1

* Thu Sep 24 2026 D3adEr1c <lqyyy0717@outlook.com> - 1.28.0-1.local
- Rebuild with updated dae-wing/dae-core
- Update cilium/ebpf for extended BTF header support

* Fri Apr 17 2026 zhullyb <zhullyb@outlook.com> - 1.27.0-1
- new version

* Wed Apr 01 2026 zhullyb <zhullyb@outlook.com> - 1.26.0-1
- new version

* Tue Mar 31 2026 zhullyb <zhullyb@outlook.com> - 1.25.0-1
- new version

* Thu Feb 19 2026 zhullyb <zhullyb@outlook.com> - 1.24.0-1
- new version

* Wed Feb 04 2026 zhullyb <zhullyb@outlook.com> - 1.23.0-1
- new version

* Tue Jan 27 2026 zhullyb <zhullyb@outlook.com> - 1.22.0-1
- new version

* Mon Dec 08 2025 zhullyb <zhullyb@outlook.com> - 1.21.1-1
- new version

* Sun Dec 07 2025 zhullyb <zhullyb@outlook.com> - 1.20.0-1
- new version

* Sat Dec 06 2025 zhullyb <zhullyb@outlook.com> - 1.19.0-1
- new version

* Fri Dec 05 2025 zhullyb <zhullyb@outlook.com>
- new version

* Thu Dec 04 2025 zhullyb <zhullyb@outlook.com> - 1.17.0-1
- new version

* Wed Dec 03 2025 zhullyb <zhullyb@outlook.com> - 1.15.1-1
- new version

* Wed Dec 03 2025 zhullyb <zhullyb@outlook.com> - 1.13.0-1
- new version

* Wed Dec 03 2025 zhullyb <zhullyb@outlook.com> - 1.10.0-1
- new version

* Tue Dec 02 2025 zhullyb <zhullyb@outlook.com> - 1.8.0-1
- new version

* Mon Dec 01 2025 zhullyb <zhullyb@outlook.com> - 1.5.1-1
- new version

* Sun Nov 30 2025 zhullyb <zhullyb@outlook.com> - 0.18.0-1
- new version

* Sun Jun 01 2025 zhullyb <zhullyb@outlook.com> - 1.0.0-1
- new version

* Wed Feb 19 2025 zhullyb
- Initial package

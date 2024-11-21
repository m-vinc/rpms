%define version 2.0.0
%define pwd %{expand:%%(pwd)}

Name:           dtui
Version:        %{version}
Release:        %autorelease
Summary:        Small TUI for introspecting the state of the system/session dbus 

License:        https://github.com/Troels51/dtui/blob/main/LICENSE
URL:            https://github.com/Troels51/dtui
%undefine _disable_source_fetch
Source0:        https://github.com/Troels51/dtui/archive/refs/tags/v%{version}.tar.gz
%define SHA256SUM0 6467ec552ea6a468841c9186599fe757f9e66380f45244cce37103cc3ed45a29

BuildRequires:  rust cargo
BuildArch:      x86_64
Provides:       %{name}

%description
A small TUI for d-termining the state of your dbus. It will show you the current services running and allow you to introspect objects and their interfaces in those services

%global debug_package %{nil}

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup

%build
cargo build \
  --profile release

%install
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/dtui %{buildroot}/usr/bin/dtui
# install -Dm 0644 %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/share/dtui/LICENSE

%files
# %license /usr/share/dtui/LICENSE
/usr/bin/dtui

%changelog
* Thu Nov 21 2024 vm
- init


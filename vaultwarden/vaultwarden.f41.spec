%define version 1.32.5
%define pwd %{expand:%%(pwd)}

Name:           vaultwarden
Version:        %{version}
Release:        %autorelease
Summary:        Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs 

License:        https://github.com/dani-garcia/vaultwarden/blob/main/LICENSE.txt
URL:            https://github.com/dani-garcia/vaultwarden
%undefine _disable_source_fetch
Source0:        https://github.com/dani-garcia/vaultwarden/archive/refs/tags/%{version}.zip
%define SHA256SUM0 3627f2471589c421f09aac9edd5cd08edc1058056ada34f47bc6664edaf4c252 

BuildRequires:  rust cargo openssl-devel postgresql-devel sqlite-devel
BuildArch:      x86_64
Provides:       %{name}

# Requires:
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
An alternative server implementation of the Bitwarden Client API, written in Rust and compatible with official Bitwarden clients [disclaimer], perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

%global debug_package %{nil}

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup

%build
cargo build \
  --features sqlite,postgresql \
  --profile release \
#  --target=%{_arch}

%install
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/vaultwarden %{buildroot}/usr/bin/vaultwarden
install -Dm 0644 %{_builddir}/%{name}-%{version}/LICENSE.txt %{buildroot}/usr/share/vaultwarden/LICENSE.txt
mkdir -p %{buildroot}/var/lib/vaultwarden

%files
%license /usr/share/vaultwarden/LICENSE.txt
/usr/bin/vaultwarden
/var/lib/vaultwarden

%pre
/usr/bin/getent group vaultwarden || /usr/sbin/groupadd -r vaultwarden
/usr/bin/getent passwd vaultwarden || /usr/sbin/useradd -g vaultwarden -r -d /var/lib/vaultwarden -s /sbin/nologin vaultwarden

# %postun
# %systemd_postun_with_stop %{name}.service
# /usr/sbin/userdel vaultwarden
# 
# %post
# %systemd_post_with_restart %{name}.service

%changelog
* Mon Oct 21 2024 vm
- init


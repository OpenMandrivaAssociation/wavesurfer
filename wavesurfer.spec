%define name	wavesurfer
%define version 1.8.5
%define release %mkrel 1

Summary:	Script-driven sound processing toolkit.
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	MIT
Group: 		Sound
URL: 		http://www.speech.kth.se/wavesurfer/
Source: 	%{name}-%{version}.tar.bz2
Source11: 	%{name}16.png
Source12: 	%{name}32.png
Source13: 	%{name}48.png
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libsnack tcl tk
BuildArch:	noarch

%description
WaveSurfer is an Open Source tool for sound visualization and manipulation.
It has been designed to suit both novice and advanced users. WaveSurfer has
a simple and logical user interface that provides functionality in an
intuitive way and which can be adapted to different tasks. It can be used
as a stand-alone tool for a wide range of tasks in speech research and
education. Typical applications are speech/sound analysis and sound
annotation/transcription. WaveSurfer can also serve as a platform for more
advanced/specialized applications. This is accomplished either through
extending the WaveSurfer application with new custom plug-ins or by
embedding WaveSurfer visualization components in other applications.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -r wsurf* $RPM_BUILD_ROOT%{_libdir}
install -m755 %{name}.tcl -D $RPM_BUILD_ROOT/%{_bindir}/%{name}

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="wavesurfer" \
needs="x11" \
section="Multimedia/Sound" \
title="WaveSurfer" \
icon="wavesurfer.png" \
longtitle="Graphical sound editor"
EOF

#icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc doc/* LICENSE.txt README.txt 
%{_bindir}/%{name}
%{_libdir}/wsurf*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}

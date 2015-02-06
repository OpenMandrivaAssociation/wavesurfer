%define name	wavesurfer
%define version 1.8.5
%define release 6

Summary:	Script-driven sound processing toolkit
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
Requires:	tcl-snack tk
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
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
cp -r wsurf* $RPM_BUILD_ROOT%{_prefix}/lib
install -m755 %{name}.tcl -D $RPM_BUILD_ROOT/%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=WaveSurfer
Comment=Graphical sound editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Audio;Player;X-MandrivaLinux-Multimedia-Audio;AudioVideo;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc doc/* LICENSE.txt README.txt 
%{_bindir}/%{name}
%{_prefix}/lib/wsurf*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8.5-5mdv2010.0
+ Revision: 434702
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.8.5-4mdv2009.0
+ Revision: 242968
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 12 2007 Olivier Blin <oblin@mandriva.com> 1.8.5-2mdv2008.0
+ Revision: 51553
- use /usr/lib instead of libdir, it is a noarch package (thanks Goetz)

* Fri Apr 20 2007 Olivier Blin <oblin@mandriva.com> 1.8.5-1mdv2008.0
+ Revision: 16012
- XDG menu
- require tcl-snack
- 1.8.5
- Import wavesurfer



* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6.4-1mdk
- 1.6.4
- cosmetics

* Fri May 14 2004 Michael Scherer <misc@mandrake.org> 1.6.3-1mdk
- New release 1.6.3
- correct menu problem

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 1.6.2-1mdk
- 1.6.2

* Fri Sep 5 2003 Austin Acton <aacton@yorku.ca> 1.5.3-1mdk
- 1.5.3

* Mon Jul 7 2003 Austin Acton <aacton@yorku.ca> 1.5.2-1mdk
- 1.5.2

* Sun Jun 8 2003 Austin Acton <aacton@yorku.ca> 1.5.1-1mdk
- 1.5.1
- fix icon names
- noarch

* Sat Jan 11 2003 Austin Acton <aacton@yorku.ca> 1.4.6-1mdk
- initial package

Summary:	"UFO: Alien Invasion" is a squad-based tactical strategy game in the tradition of the old X-COM PC games
Name:		ufoai
Version:	2.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
URL:		http://ufoai.sourceforge.net/
Source0:	http://dl.sourceforge.net/ufoai/%{name}-%{version}-source.tar.bz2
# Source0-md5:	67347e7124fe5679c672a392161a6611
Source1:	%{name}.desktop
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	ufoai-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is the year 2084. You control a secret organisation charged with
defending Earth from a brutal alien enemy. Build up your bases,
prepare your team, and dive head-first into the fast and flowing
turn-based combat.

"UFO: Alien Invasion" is a squad-based tactical strategy game in the
tradition of the old X-COM PC games, but with a twist. This game
combines military realism with hard science-fiction and the weirdness
of an alien invasion. The carefully constructed turn-based system
gives you pin-point control of your squad while maintaining a sense of
pace and danger.

Over the long term you will need to conduct research into the alien
threat to figure out their mysterious goals and use their powerful
weapons for your own ends. You will produce unique items and use them
in combat against your enemies. If you like, you can even use them
against your friends with multiplayer functionality.

"UFO: Alien Invasion". Endless hours of gameplay -- absolutely free.

%prep
%setup -q -n %{name}-%{version}-source

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--enable-mmx \
	--with-curses \
	--with-shaders
%{__make}
%{__make} lang

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/base,%{_datadir}/%{name}/base/i18n,%{_pixmapsdir},%{_desktopdir}}
install base/game.so $RPM_BUILD_ROOT%{_libdir}/%{name}/base/game.so
install ufo $RPM_BUILD_ROOT%{_libdir}/%{name}/ufoai
install ufoded $RPM_BUILD_ROOT%{_libdir}/%{name}/ufoaided
install ufo2map $RPM_BUILD_ROOT%{_bindir}/ufoai2map
cp -a base/i18n $RPM_BUILD_ROOT%{_datadir}/%{name}/base

cat > ufoai << 'EOF'
#!/bin/sh
cd %{_libdir}/%{name}
exec ./ufoai
EOF
cat > ufoaided << 'EOF'
#!/bin/sh
cd %{_libdir}/%{name}
exec ./ufoaided
EOF

install ufoai $RPM_BUILD_ROOT%{_bindir}/ufoai
install ufoaided $RPM_BUILD_ROOT%{_bindir}/ufoaided

ln -s %{_datadir}/%{name}/base/i18n $RPM_BUILD_ROOT%{_libdir}/%{name}/base/i18n
for i in 0base 0maps 0media 0models 0music 0pics 0snd 0ufos; do
	ln -s %{_datadir}/%{name}/base/$i.pk3 $RPM_BUILD_ROOT%{_libdir}/%{name}/base/$i.pk3
done

# install icon and desktop file
install src/ports/linux/installer/data/ufo.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufoai
%attr(755,root,root) %{_bindir}/ufoaided
%attr(755,root,root) %{_bindir}/ufoai2map
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/ufoai
%attr(755,root,root) %{_libdir}/%{name}/ufoaided
%dir %{_libdir}/%{name}/base
%attr(755,root,root) %{_libdir}/%{name}/base/game.so
%attr(755,root,root) %{_libdir}/%{name}/base/i18n
%attr(755,root,root) %{_libdir}/%{name}/base/*.pk3
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/base
%{_datadir}/%{name}/base/i18n
%{_pixmapsdir}/%{name}.xpm
%{_desktopdir}/%{name}.desktop

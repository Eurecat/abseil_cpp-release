Name:           ros-lunar-abseil-cpp
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS abseil_cpp package

Group:          Development/Libraries
License:        Apache
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-lunar-catkin
BuildRequires:  rsync

%description
The abseil_cpp package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Nov 15 2017 dfaconti <davide.faconti@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Nov 14 2017 dfaconti <davide.faconti@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Fri Oct 13 2017 dfaconti <davide.faconti@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Sun Oct 01 2017 dfaconti <davide.faconti@gmail.com> - 0.1.1-0
- Autogenerated by Bloom


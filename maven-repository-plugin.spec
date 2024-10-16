%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-repository-plugin
Version:        2.3.1
Release:        10.0%{?dist}
Summary:        Plugin to create bundles of artifacts for manual uploaded to repository


License:        ASL 2.0
URL:            https://maven.apache.org/plugins/maven-repository-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         add_compat.patch
BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven-shared-verifier
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires: java

Obsoletes: maven2-plugin-repository <= 0:2.0.8
Provides: maven2-plugin-repository = 1:%{version}-%{release}

%description
This plugin is used to create bundles of artifacts that 
can be uploaded to the central repository.

%package javadoc

Summary:        Javadoc for %{name}
Requires: jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-10
- Build using xmvn.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3.1-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-4
- Fix building/working in pure maven3 environment.

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-3
- Build with maven 3.x.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- Update to 2.3.1.

* Wed Sep 15 2010 Yong Yang <yyang@redhat.com> 2.3-3
- BR: maven-shared-verifier
- Add dep wagon-provider-api by patch

* Mon Jun 07 2010 Yong Yang <yyang@redhat.com> 2.3-2
- Update summary due to length issue
- Add LICENSE.txt

* Fri Jun 04 2010 Yong Yang <yyang@redhat.com> 2.3-1
- Initial package.

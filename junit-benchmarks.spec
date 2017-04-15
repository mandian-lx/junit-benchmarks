%{?_javapackages_macros:%_javapackages_macros}

Name:          junit-benchmarks
Version:       0.7.2
Release:       0 #7%{?dist}
Summary:       Code benchmarking in JUnit4
Group:         Development/Java
License:       ASL 2.0
URL:           http://labs.carrotsearch.com/junit-benchmarks.html
Source0:       https://github.com/carrotsearch/junit-benchmarks/archive/release/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

# test deps
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(jaxen:jaxen)
BuildRequires: mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
%if 0
BuildRequires: mvn(mysql:mysql-connector-mxj:5.0.12)
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M10)
%endif
BuildRequires: xmvn

BuildArch:     noarch

%description
A framework for writing performance micro-benchmarks using JUnit4 annotations.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-release-%{version}

%pom_remove_plugin :maven-clover2-plugin
# require retrotranslator
%pom_remove_plugin :maven-antrun-plugin

%pom_remove_dep mysql:mysql-connector-mxj
%pom_remove_dep org.easytesting:fest-assert-core
rm src/test/java/com/carrotsearch/junitbenchmarks/TestAssumptions.java

# AssertionError with new h2 release
rm -r src/test/java/com/carrotsearch/junitbenchmarks/h2 \
 src/test/java/com/carrotsearch/junitbenchmarks/examples/ArrayListIterationBenchmark.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc junit-benchmarks.LICENSE

%files javadoc -f .mfiles-javadoc
%doc junit-benchmarks.LICENSE

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 gil cattaneo <puntogil@libero.it> 0.7.2-6
- disable h2 test suite

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 09 2015 gil cattaneo <puntogil@libero.it> 0.7.2-3
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 gil cattaneo <puntogil@libero.it> 0.7.2-1
- update to 0.7.2

* Fri Sep 14 2012 gil cattaneo <puntogil@libero.it> 0.4.0-1
- initial rpm

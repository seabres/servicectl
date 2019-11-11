#!/bin/sh
rpmbuild -v --define "_topdir $PWD" -bb servicectl.spec
rm -rf SRPMS BUILDROOT SOURCES SPECS BUILD

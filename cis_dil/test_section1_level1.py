"""
module for testing cis_dil
"""
import logging
import pytest
import testinfra


@pytest.mark.cis_dil
@pytest.mark.cis_dil_section1
@pytest.mark.cis_dil_level1
class TestSection1Level1:
    """
    Test class for cis_dil section1 level1 tests
    """

    @pytest.mark.dil_1_1_1_1_ensure_cramfs_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_1_ensure_cramfs_disabled(self, host):
        """
        1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The cramfs filesystem type is a compressed read-only Linux filesystem embedded in small
        footprint systems. A cramfs image can be used without having to first decompress the
        image.
        Rationale:
        Removing support for unneeded filesystem types reduces
        """
        cmd = host.run('modprobe -n -v cramfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep cramfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_2_ensure_freevxfs_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_2_ensure_freevxfs_disabled(self, host):
        """
        1.1.1.2 Ensure mounting of freevxfs filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The freevxfs filesystem type is a free version of the Veritas type filesystem. This is the
        primary filesystem type for HP-UX operating systems.
        Rationale:
        Removing support for unneeded filesystem types reduces the local attack surface of the
        system. If this filesystem type is not needed, disable it.
        """
        cmd = host.run('modprobe -n -v freevxfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep freevxfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)


    @pytest.mark.dil_1_1_1_3_ensure_jffs2_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_3_ensure_jffs2_disabled(self, host):
        """
        1.1.1.3 Ensure mounting of jffs2 filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The jffs2 (journaling flash filesystem 2) filesystem type is a log-structured filesystem used
        in flash memory devices.
        Rationale:
        Removing support for unneeded filesystem types reduces the local attack surface of the
        system. If this filesystem type is not needed, disable it.
        """
        cmd = host.run('modprobe -n -v jffs2')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep jffs2')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_4_ensure_hfs_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_4_ensure_hfs_disabled(self, host):
        """
        1.1.1.4 Ensure mounting of hfs filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The hfs filesystem type is a hierarchical filesystem that allows you to mount Mac OS
        filesystems.
        Rationale:
        Removing support for unneeded filesystem types reduces
        """
        cmd = host.run('modprobe -n -v hfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep hfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_5_ensure_hfsplus_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_5_ensure_hfsplus_disabled(self, host):
        """
        1.1.1.5 Ensure mounting of hfsplus filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The hfsplus filesystem type is a hierarchical filesystem designed to replace hfs that allows
        you to mount Mac OS filesystems.
        Rationale:
        Removing support for unneeded filesystem types reduces the local attack surface of the
        system. If this filesystem type is not needed, disable it.
        """
        cmd = host.run('modprobe -n -v hfsplus')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep hfsplus')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_6_ensure_squashfs_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_6_ensure_squashfs_disabled(self, host):
        """
        1.1.1.6 Ensure mounting of squashfs filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The squashfs filesystem type is a compressed read-only Linux filesystem embedded in
        small footprint systems (similar to cramfs ). A squashfs image can be used without having
        to first decompress the image.
        Rationale:
        Removing support for unneeded filesystem types reduces
        """
        cmd = host.run('modprobe -n -v squashfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep squashfs')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_7_ensure_udf_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_7_ensure_udf_disabled(self, host):
        """
        1.1.1.7 Ensure mounting of udf filesystems is disabled (Scored)
        Profile Applicability:
         Level 1 - Server
         Level 1 - Workstation
        Description:
        The udf filesystem type is the universal disk format used to implement ISO/IEC 13346 and
        ECMA-167 specifications. This is an open vendor filesystem type for data storage on a
        broad range of media.
        """
        cmd = host.run('modprobe -n -v udf')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep udf')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

    @pytest.mark.dil_1_1_1_8_ensure_vfat_disabled
    @pytest.mark.scored
    @pytest.mark.level1_server
    @pytest.mark.level1_workstation
    def test_dil_1_1_1_8_ensure_vfat_disabled(self, host):
        """
        1.1.1.8 Ensure mounting of FAT filesystems is limited (Not Scored)
        Profile Applicability:
         Level 2 - Workstation
         Level 2 - Server
        Description:
        The FAT filesystem format is primarily used on older windows systems and portable USB
        drives or flash modules. It comes in three types FAT12 , FAT16 , and FAT32 all of which are
        supported by the vfat kernel module.
        Rationale:
        Removing support for unneeded filesystem types reduces
        """
        cmd = host.run('modprobe -n -v vfat')
        pytest.assume(cmd.rc == 0)
        pytest.assume('install /bin/true' in cmd.stdout)

        cmd = host.run('lsmod | grep vfat')
        pytest.assume(cmd.rc == 0)
        pytest.assume(cmd.stdout is None)

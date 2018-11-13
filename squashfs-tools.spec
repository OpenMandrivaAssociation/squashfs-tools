%define oname squashfs
%define _disable_ld_no_undefined 1

Name:		%{oname}-tools
Version:	4.3
Release:	15
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/%{oname}%{version}.tar.gz
# (tpg) patches from upstream git
Patch0:		0000-mksquashfs-fix-phys-mem-calculation-for-32-bit-proce.patch
Patch1:		0001-mksquashfs-ensure-value-does-not-overflow-a-signed-i.patch
Patch2:		0002-mksquashfs-fix-abort-on-failure-to-get-physical-memo.patch
Patch3:		0003-actions-add-new-exists-test-operator-for-symbolic-li.patch
Patch4:		0004-actions-add-new-absolute-test-operator-for-symbolic-.patch
Patch5:		0005-actions-add-new-contained-test-operator-for-symbolic.patch
Patch6:		0006-actions-deal-with-the-unlikely-case-readlink-returns.patch
Patch7:		0007-actions-readlink-doesn-t-0-terminate-the-returned-pa.patch
Patch8:		0008-actions-fix-empty-action.patch
Patch9:		0009-actions-fix-file-type-test.patch
Patch10:	0010-actions-add-dir_ent-to-action_data-structure.patch
Patch11:	0011-actions-add-new-contained_followlink-test-operator-f.patch
Patch12:	0012-actions-contained-should-check-for-nonstandard_pathn.patch
Patch13:	0013-actions-optimise-string-handling-in-follow_link.patch
Patch14:	0014-actions-use-access-as-an-initial-validity-check-in-c.patch
Patch15:	0015-actions-implement-stat-expr-eval-expr-on-the-file-po.patch
Patch16:	0016-actions-add-a-prune-action-allow-fine-tuning-of-excl.patch
Patch17:	0017-mksquashfs-move-symlink-reading-from-create_inode-to.patch
Patch18:	0018-action-add-code-to-check-test-is-correct-for-action-.patch
Patch19:	0019-action-update-absolute-test-to-use-in-core-directory.patch
Patch20:	0020-mksquashfs-move-creation-of-root-directory-dir_ent-a.patch
Patch21:	0021-actions-rewrite-exists-test-operation.patch
Patch22:	0022-actions-get-rid-of-contained-and-contained_followlin.patch
Patch23:	0023-action-implement-readlink-test-operation.patch
Patch24:	0024-actions-fix-uid-so-it-takes-a-name-rather-than-just-.patch
Patch25:	0025-actions-fix-gid-so-it-takes-a-name-rather-than-just-.patch
Patch26:	0026-action-parse_gid.patch
Patch27:	0027-action-add-comment-describing-generic-TEST_VAR_FN-ma.patch
Patch28:	0028-action-add-dircount-test-operation.patch
Patch29:	0029-mksquashfs-fix-dir_scan5-empty-prune-action.patch
Patch30:	0030-action-add-dircount_range-test-operation.patch
Patch32:	0032-mksquashfs-actions-make-the-root-of-the-in-core-dire.patch
Patch60:	0060-action-in-eval_XXX_action-functions-strdup-sub-pathn.patch
Patch61:	0061-action-stat_fn-should-be-using-it-s-own-copy-of-stru.patch
Patch62:	0062-action-readlink_fn-should-be-using-it-s-own-copy-of-.patch
Patch63:	0063-action-add-eval-test-operation.patch
Patch64:	0064-actions-implement-verbose_action-option.patch
Patch65:	0065-actions-implement-verbose_action-for-eval_fn-test-op.patch
Patch66:	0066-actions-implement-verbose_action-for-readlink_fn-tes.patch
Patch67:	0067-actions-implement-verbose_action-for-stat_fn-test-op.patch
Patch68:	0068-actions-implement-vaf-verbose-action-file-option.patch
Patch69:	0069-action-extend-logging-to-handle-log-if-action-TRUE-a.patch
Patch70:	0070-action-update-action-option-parsing-to-use-ACTION_LO.patch
Patch71:	0071-action-make-action_read_file-use-ACTION_LOG_-NONE-VE.patch
Patch72:	0072-mksquashfs-add-true_action-option.patch
Patch73:	0073-mksquashfs-add-false_action-option.patch
Patch74:	0074-mksquashfs-add-action_file-as-synonym-for-af.patch
Patch75:	0075-mksquashfs-add-verbose_action_file-as-synonym-for-va.patch
Patch76:	0076-mksquashfs-fix-read_action_file-to-use-ACTION_LOG_-N.patch
Patch77:	0077-mksquashfs-add-true_action_file-option.patch
Patch78:	0078-mksquashfs-add-true-action-file-option.patch
Patch79:	0079-mksquashfs-fix-usage-of-_-in-new-options.patch
Patch80:	0080-mksquashfs-add-false-action-file-option.patch
Patch81:	0081-actions-eval_expr_top-should-be-using-subpath-and-no.patch
Patch82:	0082-actions-fix-those-underscores.patch
Patch83:	0083-actions-fix-symbolic-mode-parsing-in-the-mode-action.patch
Patch84:	0084-action-add-chmod-as-a-synonym-for-mode.patch
Patch85:	0085-action-expression-logging-should-be-using-action-arg.patch
Patch86:	0086-actions-Regularise-SYNTAX_ERROR-statements.patch
Patch87:	0087-actions-Regularise-SYNTAX_ERROR-statements.patch
Patch88:	0088-mksquashfs-fix-cmdline-arg-free-if-1-source-dir-and-.patch
Patch89:	0089-action-split-the-execute-mode-code-out-of-mode_actio.patch
Patch90:	0090-actions-update-test-function-parser-to-handle-variab.patch
Patch91:	0091-action-fix-move-argument-parsing.patch
Patch92:	0092-actions-implement-perm-test-function.patch
Patch93:	0093-actions-refactor-parse_octal_mode_args-to-use-it-wit.patch
Patch94:	0094-action-add-octal-mode-support-to-perm-test-function.patch
Patch95:	0095-action-chmod-fix-mode-setting-if-octal-value-specifi.patch
Patch96:	0096-action-change-expression-logging-to-use-atom-args.patch
Patch97:	0097-actions-change-expression-logging-to-not-print-brack.patch
Patch98:	0098-actions-add-new-noop-action.patch
Patch99:	0099-mksquashfs-fix-progressbar-for-sort-files.patch
Patch100:	0100-mksquashfs-fix-rare-race-in-fragment-waiting-in-file.patch
Patch101:	0101-Fix-2GB-limit-of-the-is_fragment-.-function.patch
Patch102:	0102-mksquashfs-fix-compilation-on-older-toolchains.patch
Patch103:	0103-pseudo-Add-support-for-pseudo-file-symlinks.patch
Patch104:	0104-mksquashfs-Fix-segfault-when-SQUASHFS_TRACE-is-enabl.patch
Patch105:	0105-unsquashfs-modify-xattrs-after-other-changes.patch
Patch106:	0106-fix-device-type-handling-with-extended-attributes.patch
Patch107:	0107-squashfs-tools-with-fnmatch.h-compatibility-with-mus.patch
Patch108:	0108-pseudo.c-add-explicit-sys-stat.h-include.patch
Patch109:	0109-mksquashfs-enable-quiet-option.patch
Patch110:	0110-unsquashfs-add-code-to-dump-the-exact-bytes-used.patch
Patch111:	0111-Add-offset-option-to-skip-n-bytes-at-the-start-of-th.patch
Patch112:	0112-Add-offset-function-to-skip-n-bytes-at-the-beginning.patch
Patch113:	0113-pseudo-Add-missing-line-termination-in-ERROR.patch
Patch114:	0114-Fix-compile-warnings-introduced-with-the-quiet-optio.patch
Patch115:	0115-pseudo-handle-quoted-filenames.patch
Patch116:	0116-Pseudo-improve-the-error-message-when-filenames-with.patch
Patch117:	0117-mksquashfs-add-pseudo-definition-format-to-the-help-.patch
Patch118:	0118-pseudo.c-Fix-pseudo-format-error-message.patch
Patch119:	0119-mksquashfs-Make-all-compressor-functions-static.patch
Patch120:	0120-squashfs-tools-Add-zstd-support.patch
# And our own patches...
Patch200:	squashfs-4.3-glibc-2.28.patch

BuildRequires:	pkgconfig(zlib)
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig(libzstd)

%description
squashfs-tools are utilities for the creation
of compressed squashfs images.

%prep
%setup -q -n %{oname}%{version}
%apply_patches

%build
%setup_compile_flags

cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make -j1 ZSTD_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 LZ4_SUPPORT=1 COMP_DEFAULT=zstd EXTRA_CFLAGS="%{optflags}"

%install
install -m755 squashfs-tools/mksquashfs -D %{buildroot}%{_bindir}/mksquashfs
install -m755 squashfs-tools/unsquashfs -D %{buildroot}%{_bindir}/unsquashfs

%files
%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs

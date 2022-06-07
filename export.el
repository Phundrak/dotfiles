#!/usr/bin/env -S emacs -Q --script

(require 'package)
(require 'org)
(require 'ox-html)

(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
(package-initialize)
(package-refresh-contents)
(package-install 'htmlize)

(setq org-confirm-babel-evaluate nil
      org-html-validation-link nil
      make-backup-files nil)

(defun export-and-clean (directory)
  (progn  (mapc (lambda (file)
                  (progn (message (concat "=====================\n"
                                          "Exporting "
                                          file
                                          "\n"
                                          "=====================\n"))
                         (with-current-buffer (find-file file)
                           (org-html-export-to-html))))
                (directory-files directory t (regexp-quote ".org")))))

(dolist (dir '("org/config/" "org/config/Deprecated/" "org/config/WIP"))
  (export-and-clean dir))

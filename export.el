#!/usr/bin/emacs --script
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)
(package-refresh-contents)
(package-install 'htmlize)
(package-install 's)
(require 's)
(setq org-confirm-babel-evaluate nil
      org-html-validation-link nil)
(let* ((files (mapcar #'expand-file-name
                      (file-expand-wildcards "org/config/*.org"))))
  (mapc (lambda (file)
          (message (format "==========\nExporting %S\n==========" file))
          (with-current-buffer (find-file file)
            (org-html-export-to-html)))
        files))
(let* ((files (mapcar #'expand-file-name
                      (file-expand-wildcards "org/config/*.html~"))))
  (mapc (lambda (file)
          (delete-file file))
        files))

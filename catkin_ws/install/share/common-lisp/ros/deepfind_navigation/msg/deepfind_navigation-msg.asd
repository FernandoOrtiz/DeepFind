
(cl:in-package :asdf)

(defsystem "deepfind_navigation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "encoders_data" :depends-on ("_package_encoders_data"))
    (:file "_package_encoders_data" :depends-on ("_package"))
  ))
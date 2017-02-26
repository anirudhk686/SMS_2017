 function register() {
 $.ajax({
                url: "url",
                type: 'POST',
                dataType: "html",
                data:{id:params},
                success: function(data, status, xhr) {
                    if(data==""){
                        window.location.href="/";
                    }
                    else{
                        BootstrapDialog.show({
                            title: "Registration Successful",
                            message: function(dialogRef){
                                $mydata = $($.parseHTML(data));
                                return $mydata;
                            },
                            onshow: function(dialog){

                        // and css change if need, eg. 
                         dialog.$modalHeader.css("float","none");

                            },
                            onshown:function(dialog)
                            {
                               // event after shown

                            },
                            onhide:function(dailog)
                            {
                               // event on hide
                            }
                        });
                    }

                },
            });
 }
var sample = {
    // 封装样例相关ajax的URL
    URL : {

    },
    // 验证手机号
    validatePhone : function (phone) {
        if(phone && phone.length == 11 && !isNaN(phone)) {
            return true;
        } else {
            return false;
        }
    },
    // 详情页秒杀逻辑
    detail : {
        // 详情页初始化
        init : function (params) {
           //手机验证和登录，计时交互
            var userPhone = $.cookie("userPhone");
            var startTime = params['startTime'];
            var endTime = params['endTime'];
            var sampleId = params['sampleId'];
            if(!sample.validatePhone(userPhone)) {
                var userPhoneModal = $('#userPhoneModal');
                userPhoneModal.modal({
                    show : true,//显示弹出层
                    backdrop : 'static',//禁止位置关闭
                    keyboard : false//关闭键盘事件
                });
                $('#userPhoneBtn').click(function () {
                    var inputPhone = $('#userPhoneKey').val();
                    if(sample.validatePhone(inputPhone)) {
                        //电话写入cookie
                        $.cookie('userPhone', inputPhone, {expires: 7, path: '/sample'});
                        // 刷新页面
                        window.location.reload();
                    } else {
                        $('#userPhoneMessage').hide().html('<label class="label label-danger">手机号错误</label>').show(300);
                    }
                });
            }
        }
    }
};
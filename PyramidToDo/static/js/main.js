new Vue({
    el: '#main',
    data: {
        new_task_text: '',
        tasks: []
    },
    methods: {
        get_all: function () {
            this.tasks = [];
            var req = new XMLHttpRequest();
            req.open("GET", "api/get-all", false);
            req.send(null);
            this.tasks = JSON.parse(req.response).data;
        },
        add_new_task: function () {
            var req = new XMLHttpRequest();
            req.open("POST", "api/add?task=" + this.new_task_text, false);
            req.send(null);
            this.new_task_text = '';
            this.get_all();
        },
        update_state: function (task) {
            var req = new XMLHttpRequest();
            req.open("PUT", "api/update?id=" + task[0] + "&state=" + !task[1], false);
            task[1] = !task[1];
            req.send(null);
            this.get_all();
        },
        delete_task: function (task) {
            var req = new XMLHttpRequest();
            req.open("POST", "api/delete?id=" + task[0], false);
            req.send();
            this.get_all();
        },
        clear_field: function () {
            this.new_task_text = '';
        },
    },
    mounted: function () {
        this.get_all();
    }
})
angular.module('lite_app', [])
.controller('liteCtrl', [function(){
    var self = this;
    self.notes = [
        {id: 1, label: 'First Note', done: false},
        {id: 2, label: 'Second Note', done: false},
        {id: 3, label: 'Third Note', done: true}
    ];
}]);

var columns = [
	{id:'name', name:'Name', field:'name'},
	{id:'clevel', name:'Level', field:'clevel'},
	{id:'team', name:'Team', field: 'team'},
	{id: 'manager', name: 'Manager', field: 'manager'},
	{id: 'join_dt', name: 'Joined on', field: 'join_dt'}
	];

var staffs = [
	{name:'Jin, Li',clevel:'C13', team:'TIP', manager:'Dong, Wei', join_dt:'01/01/2017'},
	{name:'Shang, Jialiang',clevel:'C12', team:'DS', manager:'Dong, Wei', join_dt:'01/01/2016'},
	{name:'Li, Queenie',clevel:'C12', team:'QA', manager:'Dong, Wei', join_dt:'01/01/2017'},
	{name:'Lu, Zhouhao',clevel:'C12', team:'DT', manager:'Dong, Wei', join_dt:'01/01/2017'},
	{name:'Zhong, Jacob',clevel:'C12', team:'CP', manager:'Dong, Wei', join_dt:'01/01/2017'},
	{name:'Zheng, Pei',clevel:'C12', team:'OC', manager:'Dong, Wei', join_dt:'01/01/2017'},
	{name:'Lu, Jian',clevel:'C14', team:'FxRD', manager:'Chen, Arthur', join_dt:'01/01/2017'},
	{name:'Dong, Wei',clevel:'C14', team:'Muni', manager:'Chen, Arthur', join_dt:'01/01/2017'}
	];

var options = {
	enableCellNavigation: true,
	enableColumnReorder: false
};

var slickgrid = new Slick.Grid("#myteam", staffs, columns, options);

// $(".data .filter").append('test 123');
angular.module('lite_app', [])
.controller('liteCtrl', ['D3Service', function(D3Service){
    var self = this;

    self.staff_fields = [
        {id: 1, label: 'name', checked: true},
        {id: 2, label: 'clevel', checked: true},
        {id: 3, label: 'team', checked: true},
        {id: 4, label: 'manager', checked: true},
        {id: 5, label: 'join_dt', checked: true},
        {id: 6, label: 'status', checked: false},
        {id: 7, label: 'salary', checked: false},
        {id: 8, label: 'phone', checked: false}
    ];
    self.nav_menu_items = [
    	{label: 'Teams', url: '#'},
    	{label: 'Applications', url: '#'},
    	{label: 'Data Dict', url: '#'},
    	{label: 'BOW', url: '#'},
    	{label: 'Config', url: '#'}
    ];

    self.chunk = function(arr, size) {
    	var newArr = [];
    	for (var i=0; i<arr.length; i+=size) {
    		newArr.push(arr.slice(i, i+size))
    	}
    	return newArr;
    };

    self.team_data = {
    	columns: [
			{id:'name', name:'Name', field:'name'},
			{id:'clevel', name:'Level', field:'clevel'},
			{id:'team', name:'Team', field: 'team'},
			{id: 'manager', name: 'Manager', field: 'manager'},
			{id: 'join_dt', name: 'Joined on', field: 'join_dt'}
		],
		staffs: [
			{name:'Jin, Li',clevel:'C13', team:'TIP', manager:'Dong, Wei', join_dt:'01/01/2017'},
			{name:'Shang, Jialiang',clevel:'C12', team:'DS', manager:'Dong, Wei', join_dt:'01/01/2016'},
			{name:'Li, Queenie',clevel:'C12', team:'QA', manager:'Dong, Wei', join_dt:'01/01/2017'},
			{name:'Lu, Zhouhao',clevel:'C12', team:'DT', manager:'Dong, Wei', join_dt:'01/01/2017'},
			{name:'Zhong, Jacob',clevel:'C12', team:'CP', manager:'Dong, Wei', join_dt:'01/01/2017'},
			{name:'Zheng, Pei',clevel:'C12', team:'OC', manager:'Dong, Wei', join_dt:'01/01/2017'},
			{name:'Lu, Jian',clevel:'C14', team:'FxRD', manager:'Chen, Arthur', join_dt:'01/01/2017'},
			{name:'Dong, Wei',clevel:'C14', team:'Muni', manager:'Chen, Arthur', join_dt:'01/01/2017'}
		]
    };

    self.init_team_data = function(locator){
    	var options = {
			enableCellNavigation: true,
			enableColumnReorder: false
		};
		var slickgrid = new Slick.Grid(locator, self.team_data.staffs, self.team_data.columns, options);
		return slickgrid;
    }
    self.updateGrid = function($event, id){
    	console.log(id);
    }

    self.staff_fields_filter = self.chunk(self.staff_fields, 2);
    self.slickgrid = self.init_team_data("#myteam");

    D3Service.show();

}]).factory('D3Service', ['$log', function($log){
    var d = d3;
    return {
        show: function() {
            $log.log('call D3 service');
            d.select('.utest').style('background', 'black');
        }
    }
}]);






// $(".data .filter").append('test 123');
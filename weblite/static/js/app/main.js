angular.module('lite_app', [])
.controller('liteCtrl', [function(){
    var self = this;
    self.notes = [
        {id: 1, label: 'First Note', done: false},
        {id: 2, label: 'Second Note', done: false},
        {id: 3, label: 'Third Note', done: true}
    ];
}]);

describe('Controller:LiteCtrl', function(){

    beforeEach(module('lite_app'));

    var ctrl;

    beforeEach(inject(function($controller){
        ctrl = $controller('liteCtrl');
    }));

    it('should contain notes', function(){
        expect(ctrl.notes).toEqual([
            {id: 1, label: 'First Note', done: false},
            {id: 2, label: 'Second Note', done: false},
            {id: 3, label: 'Third Note', done: true}
        ]);
    });

})
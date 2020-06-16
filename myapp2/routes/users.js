var express = require('express');
var router = express.Router();
const userController = require('../controllers/users');

router.get('/', userController.index);
router.get('/add', userController.add);
router.get('/delete', userController.delete);
router.get('/edit', userController.edit);

module.exports = router;
module.exports = {
    index(req, res){
      return res.status(200).send('respond with a resource');
    }
  }

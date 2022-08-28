const {exec, execSync} = require('child_process');
const options = {stdio: 'inherit'};

export default () => {
	try {
		execSync(`cd skype-bot; ./start.sh`, options);
	} catch (error) {
		console.log('YIKES ERROR.... ~SAHIL', error);
	}
};

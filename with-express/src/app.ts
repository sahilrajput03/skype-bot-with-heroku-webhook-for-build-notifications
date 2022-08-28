import express, {Application, Request, Response} from 'express';
import fs from 'fs';
import sendSkypeMessage from './sendSkypeMessage';

// const write = (fileName: any, data: any) => {
// 	fs.writeFileSync(fileName, JSON.stringify(data));
// };

// console.log(buildSuccessful.action);
// console.log(buildSuccessful.resource);

const app: Application = express();

const port: number = Number(process.env.PORT) || 3002;

app.use(express.json());
app.post('/totel', notificationController);

app.listen(port, function () {
	console.log(`App is listening on port ${port} !`);
});

function notificationController(req: Request, res: Response) {
	const {action, resource} = req.body;
	// console.log('INFO:', {action, resource});

	// To log the entire request data in files
	// write(Math.random() + '.ts', req.body);

	sendSkypeMessage();

	if (resource === 'build') {
		// req.data.status: 'pending', 'failed', 'succeeded'
		const {status} = req.body.data;

		if (status === 'pending') {
			console.log('Build started!!');
		} else if (status === 'failed') {
			console.log('Build failed!');
		} else if (status === 'succeeded') {
			console.log('Build succeeded!');
		}
		res.send('Yo');
	} else {
		res.send('Never mind.');
	}
}

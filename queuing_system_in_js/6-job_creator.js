import kue from 'kue';

const queue = kue.createQueue();

const jobData={
    phoneNumber: '47895651',
    message: 'this is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating job:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');

});

job.on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});


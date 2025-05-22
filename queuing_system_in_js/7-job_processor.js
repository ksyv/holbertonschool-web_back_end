import kue from 'kue';

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is listening for new jobs on push_notification_code (2 at a time)...');

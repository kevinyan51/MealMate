import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { Divider } from '@mui/material';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  boxShadow: 24,
  borderRadius: 2,
  p: 4,
};

export default function ButtonModal({
  cancelButtonText = 'Cancel',
  confirmButtonText = 'Confirm',
  cancelAction,
  confirmAction,
  title = 'Title',
  content = 'Content',
  openerText = 'Open modal',
  openerProps = {},
}) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  cancelAction = cancelAction || handleClose;

  return (
    <Box>
      <Button onClick={handleOpen} {...openerProps}>
        {openerText}
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            {title}
          </Typography>
          <Divider sx={{ mt: 3, mb: 3 }} />
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            {content}
          </Typography>
          <Divider sx={{ mt: 3, mb: 3 }} />
          <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
            <Button
              variant="contained"
              color="error"
              sx={{ mr: 2 }}
              onClick={cancelAction}
            >
              {cancelButtonText}
            </Button>
            <Button variant="outlined" color="success" onClick={confirmAction}>
              {confirmButtonText}
            </Button>
          </Box>
        </Box>
      </Modal>
    </Box>
  );
}

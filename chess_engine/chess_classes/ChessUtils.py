

def build_official_move(src_x, src_y, source_piece, dest_x, dest_y,
                        target_piece=None, check=None, ep=None, rook=None, promo=None):
    # print 'build_official_move: target_piece : %s' % target_piece

    if rook:
        # treat rook cases
        if abs(dest_x - src_x) == 2:
            res = 'O-O'
        elif abs(dest_x - src_x) == 3:
            res = 'O-O-O'
        else:
            res = '***warning rook: %s***' % rook
    else:
        # normal move

        # piece part
        res_piece_name = ''
        if source_piece.role.name != 'P':
            res_piece_name = source_piece.role.name

        # source coordinates
        res_source_coords = '%s%s' % (src_x, src_y)

        # potential catch
        res_catch = '-'
        if target_piece:
            res_catch = 'x'

        # target coordinates
        res_target_coords = '%s%s' % (dest_x, dest_y)

        # potential ep
        res_ep = ''
        if ep:
            res_ep = 'ep'

        # potential promotion
        res_promo = ''
        if promo:
            res_promo = promo

        # potential check
        res_check = ''
        if check:
            res_check = check   # ''/'+'/'#'

        res = '{piece_name}{source_coords}{catch}{target_coords}{ep}{promo}{check}'.format(
                piece_name=res_piece_name, source_coords=res_source_coords, catch=res_catch,
                target_coords=res_target_coords, ep=res_ep, promo=res_promo, check=res_check
        )
    return res

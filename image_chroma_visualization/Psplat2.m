
function N = Psplat2(u, v, c, bin_step, n_bins)
ub = 1 + mod(round((u) / bin_step), n_bins);
vb = 1 + mod(round((v) / bin_step), n_bins);
N = reshape(accumarray(sub2ind([n_bins, n_bins], ub(:), vb(:)), c(:), ...
                               [n_bins^2, 1]), n_bins, n_bins);

%http://matlabtricks.com/post-23/tutorial-on-matrix-indexing-in-matlab

